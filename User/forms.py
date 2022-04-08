from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from Sinov_ish.models import Talaba

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Talaba
        fields = ('username', 'email','fakultet','kurs', 'password1','password2')

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = Talaba
        fields = ('username','password')