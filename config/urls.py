from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',include("Sinov_ish.urls")),
    path('',include("User.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
