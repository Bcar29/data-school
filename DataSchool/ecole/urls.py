from django.urls import path
from .views import *


urlpatterns = [
    path('', accueil, name='home'),
    path('contact/', contact, name='contact'),
    path('about/', apropos, name='about'),
    
    path('eleve/', Espace_eleve.as_view(), name='eleve'),
    path('parent/', Espace_parent.as_view(), name='parent'),
    path('prof/', espace_prof.as_view(), name='prof'),
    path('parentAdd/', parentAdd, name='parentAdd'),
    
]