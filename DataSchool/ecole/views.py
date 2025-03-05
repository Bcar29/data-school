from django.shortcuts import render
from .models import *
# Create your views here.

def accueil(request):
    
    return render(request, 'ecole/index.html')

def contact(request):
    return render(request, 'ecole/contact.html')

def apropos(request):
    return render(request, 'ecole/about.html')

def espace_eleve(request):

    return render(request, 'ecole/espace_eleve.html')

def espace_parent(request):
    emplois = Emplois.objects.all()

    return render(request, 'ecole/espace_parent.html')

def espace_prof(request):
    return render(request, 'ecole/espace_prof.html')