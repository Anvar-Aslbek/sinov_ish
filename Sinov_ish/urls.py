from django.urls import URLPattern, path
from .views import home, jadval, search, search_baho

urlpatterns = [
    path('home/',home, name = 'home'),
    path('jadval/',jadval, name = 'jadval'),
    path('search/',search,name = 'search'),
    path('search_baho/',search_baho,name = 'search_baho')
]