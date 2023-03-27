from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)


urlpatterns = [
    path(
        "regitration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path(
        "activation/confirm/<str:token>/",
        views.ConfirmActivationApiView.as_view(),
        name="confirm-activation",
    ),
    path(
        "activation/resend/",
        views.ResendActivationApiView.as_view(),
        name="resend-activation",
    ),
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token-login",
    ),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
]
