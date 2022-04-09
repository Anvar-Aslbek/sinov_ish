from django.urls import URLPattern, path
from .views import home, jadval, search

urlpatterns = [
    path('home/',home, name = 'home'),
    path('jadval/',jadval, name = 'jadval'),
    path('search/',search,name = 'search')
]