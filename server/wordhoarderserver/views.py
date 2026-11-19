from .models import Player, PlayerScore, DayData, BattleInstance
from .serializers import PlayerSerializer, PlayerScoreSerializer, DayDataSerializer, BattleSerializer
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action, api_view, permission_classes, authentication_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import AccessToken
from datetime import datetime, timedelta, timezone
from uuid import uuid4


class PlayerViewSet(viewsets.ViewSet):
    queryset = Player.objects.all()
    # authentication_classes=[]
    serializer_class = PlayerSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """

        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request:Request):
        self.perform_authentication(request)

        admin = False
        user = None

        for a in request.authenticators:
            if isinstance(a, IsAdminUser):
                admin = True

            elif isinstance(a, JWTAuthentication):
                user = a.get_user(request.auth)

        queryset = None

        if admin:
            queryset = Player.objects.all()
        elif user != None:
            queryset = Player.objects.filter(id=user.id)
    
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request:Request):
        body = request.data

        Player.objects.create(
            username=body["username"],
            email=body["email"],
            password=make_password(body["password"]),
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

    @action(detail=True, methods=["POST"], url_path="createResetLink", url_name="createResetLink")
    def create_reset_password_link(self, request:Request, pk=None):
        # do one of 2 authentications: the first is from normal authentication
        # the second one is just from the user's username

        # if they are not logged into their account, they are able to enter their username
        self.perform_authentication(request)

        # get player from authenticator
        user = get_user(request)

        if int(pk) != user.id:
            return Response("Player ID did not match.")

        # get player object
        player = Player.objects.get(id=pk)

        return newResetLink(player)

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

@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def reset_password(request:Request, id):
    # get request body
    body = request.data

    # the request should send the id that the request was made from
    player = Player.objects.get(resetPasswordToken=id)

    # also make sure that the link hasn't expired
    if datetime.now().astimezone() > player.resetPasswordExpire or player.resetPasswordUsed == True:
        return Response("Reset Password Link has expired.")

    # update password
    player.set_password(body["newPass"])
    player.resetPasswordUsed = True
    player.save()
    
    return Response("Password has been reset sucessfully.")

# function for if the player forget their password and can't log in, just uses the players username in order to send the email to the account associated with it
@api_view(["POST"])
@permission_classes([])
@authentication_classes([])
def create_reset_link(request:Request, username):
    # get player object
    player = Player.objects.get(username=username)

    if player == None:
        return Response("No account was associated with the given username.")

    return newResetLink(player)

# helper function to set the players new reset password link and send them an email
def newResetLink(player:Player):
    player.resetPasswordToken = uuid4().hex

    # set the link to expire in an hour
    player.resetPasswordExpire = datetime.now().astimezone() + timedelta(hours=1)
    player.resetPasswordUsed = False
    player.save()

    # send link to the users email
    passlink = "http://localhost:8000/reset_password/" + player.resetPasswordToken + "/"

    player.email_user("WordHoarder Reset Password Link", "The reset password link for the WordHoarder account of: " + player.username + " is:\n\n" + passlink + "\n\nDo not share this link with anyone else.")

    return Response("Reset Password Link sent.")

# helper function that makes it easy to get a user from the authenticator
def get_user(request:Request):
    for a in request.authenticators:
        if isinstance(a, JWTAuthentication):
            return a.get_user(request.auth)