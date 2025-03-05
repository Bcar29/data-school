from django.urls import path

from .views import *

urlpatterns = [
    path("register/", Inscription, name="register"),
    path('login', Connexion, name='login' ),
    path('logout', Deconnexion, name='logout' ),
    path('changepwd', changePassword, name='changepwd' ),
    path("password-reset/", password_reset.as_view(), name="password-reset"),
    path("password-reset-confirm/<uidb64>/<token>", password_reset_confirm.as_view(), name="password-reset-confirm"),
]
 