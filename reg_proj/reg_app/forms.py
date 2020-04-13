from .models import User,UserProfileInfo
from django import forms


class UserForm(forms.ModelForm):

    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password','email')

class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model=UserProfileInfo
        fields=('profile_url','profile_pic')