
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include(('accounts.urls', 'accounts'), namespace='accounts')),
    path("", include(('ecole.urls', 'ecole'), namespace='ecole')),
]
