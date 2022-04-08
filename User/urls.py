from unicodedata import name
from django.urls import path
from .views import user_login, signup

urlpatterns = [
    path('', user_login, name="login"),
    path('signup/',signup,name='signup')
]