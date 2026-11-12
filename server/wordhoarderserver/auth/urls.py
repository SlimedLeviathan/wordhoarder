from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urls = [
    path('token/',
         jwt_views.TokenObtainPairView.as_view(),
         name ='token_obtain_pair'),
    path('token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name ='token_refresh'),

    path("login/", views.login, name="login"),
    path("register/", views.signUp, name="signUp"),
    path("getReset/", views.getReset, name="getReset"),
    path("reset/", views.reset, name="resetPass"),
]