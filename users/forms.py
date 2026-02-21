from django import forms


class LoginForm(forms.Form):
    pinfl = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())