
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from DataSchool import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(('accounts.urls', 'accounts'), namespace='accounts')),
    path("", include(('ecole.urls', 'ecole'), namespace='ecole')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
