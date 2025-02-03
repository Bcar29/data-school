from django.urls import path
from .views import *


urlpatterns = [
    path('', accueil, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', apropos, name='about')
    
]