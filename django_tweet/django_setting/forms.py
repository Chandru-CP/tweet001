from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class ChangeEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class ChangeProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']


class ChangeMobileNumberForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['mobile_number']
