from django import forms
from django.contrib.auth.forms import  PasswordResetForm, SetPasswordForm



class ResetForm(PasswordResetForm):
    email = forms.EmailField(label="E-mail")


class ResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Nouveau mot de passe", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    new_password2 = forms.CharField(label="Confirmer le nouveau", widget=forms.PasswordInput(attrs={"class": "form-control"}))
