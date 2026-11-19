"""
URL configuration for wordhoarderserver project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path
from .token.urls import urls as authUrls
from rest_framework import routers
from .views import PlayerViewSet, PlayerScoreViewSet, DayDataViewSet, BattleViewSet, reset_password, create_reset_link
from .models import Player, DayData

admin.site.register(Player)
admin.site.register(DayData)

router = routers.DefaultRouter()

router.register("players", PlayerViewSet)
router.register("playerScores", PlayerScoreViewSet)
router.register("dayData", DayDataViewSet)
router.register("battleInstances", BattleViewSet)

urlpatterns = [
    path("", lambda request: HttpResponse("Server is running!!!")),
    path("admin/", admin.site.urls),
    path("token/", include(authUrls)),
    path("models/", include(router.urls)),
    path("reset_password/<str:id>/", reset_password),
    path("create_reset_link/<str:username>/", create_reset_link)
]
