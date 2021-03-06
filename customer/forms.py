from django import forms

from .models import Customer


class LoginForm(forms.Form):
    username = forms.CharField(label="Username",
                                widget=forms.TextInput(
                                        attrs={'placeholder': 'Username'}))
    password = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                        attrs={'placeholder': 'Password'}))
