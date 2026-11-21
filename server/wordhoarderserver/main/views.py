from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..views import get_user

@api_view(["POST"])
def auth_test(request:Request):
    player = get_user(request)

    if player == None: # this might already be covered by django
        return Response("You don't have authorization to use this function.", 401)

    return Response("Good job, " +  player.username + ", you did an authenticated action.", 200)