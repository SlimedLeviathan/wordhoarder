from django.http import HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.decorators import api_view
from ..models import Player
from ..views import PlayerViewSet

@api_view(["POST"])
def login(request:Request):
    print(request)
    print(request.data)
    print(request.auth)

    return JsonResponse({
        "accessToken":"huh",
        "refreshToken":"wuh"
    })

@api_view(["POST"])
def signUp(request:Request):
    return PlayerViewSet.create(None, request)

@api_view(["GET"])
def getReset(request:Request):
    return HttpResponse("not made")

@api_view(["POST"])
def reset(request:Request):
    return HttpResponse("not made")