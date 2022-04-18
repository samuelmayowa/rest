from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='User name :')
    email = forms.EmailField(max_length=50, label='Email :')
    # first_name = forms.CharField(max_length=50, help_text='your name', label='First Name :')
    # last_name = forms.CharField(max_length=50, help_text="father's name", label='Last Name :')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')
