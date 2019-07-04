from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import KonUser

class KonUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = KonUser
        fields = ('username', 'email')

class KonUserChangeForm(UserChangeForm):

    class Meta:
        model = KonUser
        fields = ('username', 'email')