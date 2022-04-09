from django.urls import URLPattern, path
from .views import home, jadval

urlpatterns = [
    path('home/',home, name = 'home'),
    path('jadval/',jadval, name = 'jadval')
]