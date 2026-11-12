from .models import Player, PlayerScore, DayData, BattleInstance
from .serializers import PlayerSerializer, PlayerScoreSerializer, DayDataSerializer, BattleSerializer
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timedelta
from uuid import uuid4

class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        print(self.action)

        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            permission_classes = [AllowAny] # since people dont have auth before creating an account
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request:Request):
        self.perform_authentication(request)

        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request:Request):
        body = request.data

        print(body)

        Player.objects.create(
            username=body["username"],
            email=body["email"],
            password=body["password"],
        )

        return Response("User created sucessfully.")

    def retrieve(self, request:Request, pk=None):
        self.perform_authentication(request)

        queryset = Player.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlayerSerializer(user)
        return Response(serializer.data)

    def update(self, request:Request, pk=None):
        self.perform_authentication(request)

    def partial_update(self, request:Request, pk=None):
        self.perform_authentication(request)

    def destroy(self, request:Request, pk=None):
        self.perform_authentication(request)

    @action(detail=True, methods=["post"])
    def create_reset_password_link(self, request:Request, pk=None):
        # do one of 2 authentications: the first is from normal authentication
        # the second one is just from the user's username

        # if they are not logged into their account, they are able to enter their username
        
        self.perform_authentication(request)

        print(pk, request.auth)

        if pk != request.auth:
            return Response("Player ID did not match.")

        # get player object
        player = Player.objects.get(id=pk)

        # create a link for the password to be reset from
        player.resetPasswordToken = uuid4()

        # set the link to expire in an hour
        player.resetPasswordExpire = datetime.now() + timedelta(hours=1)
        player.save()

        # send link to the users email
        passlink = "localhost:8000/reset_password/" + player.resetPasswordToken

        player.user.email_user("The reset password link for the WordHoarder account of:", player.user.username ,"is:\n\n", passlink ,"\n\nDo not share this link with anyone else.")

        return Response("Reset Password Link sent.")

    @action(detail=True, methods=["post"])
    def reset_password(self, request:Request, pk=None):
        # get request body
        body = request.data

        print(body)

        print(body["resetID"])
        print(body["newPass"])

        # the request should send the id that the request was made from
        player = Player.objects.get(id=pk)
        if body["resetID"] != player.resetPasswordToken:
            return Response("Reset Password ID was incorrect.")

        # also make sure that the link hasn't expired
        if datetime.now() > player.resetPasswordExpire:
            return Response("Reset Password Link has expired.")

        # update password
        player.user.set_password(body["newPass"])
        player.save()
        
        return Response("Password has been reset sucessfully.")

class PlayerScoreViewSet(viewsets.ViewSet):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer

    def list(self, request:Request):
        # when listing, make sure to filter by the player id
        # get player id from auth token
        player = Player.objects.get(id=AccessToken.get(request.auth)["user_id"])

        queryset = PlayerScore.objects.filter(player=player)
        serializer = PlayerScoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request:Request, pk=None):
        player = Player.objects.get(id=AccessToken.get(request.auth)["user_id"])

        queryset = PlayerScore.objects.filter(player=player)
        user = get_object_or_404(queryset, pk=pk)
        serializer = PlayerScoreSerializer(user)
        return Response(serializer.data)

class DayDataViewSet(viewsets.ViewSet):
    queryset = DayData.objects.all()
    serializer_class = DayDataSerializer

    def list(self, request:Request):
        queryset = DayData.objects.all()
        serializer = DayDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request:Request, pk=None):
        queryset = DayData.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = DayDataSerializer(user)
        return Response(serializer.data)

class BattleViewSet(viewsets.ViewSet):
    queryset = BattleInstance.objects.all()
    serializer_class = BattleSerializer

    def list(self, request:Request):
        queryset = BattleInstance.objects.all()
        serializer = BattleSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request:Request, pk=None):
        queryset = BattleInstance.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = BattleSerializer(user)
        return Response(serializer.data)