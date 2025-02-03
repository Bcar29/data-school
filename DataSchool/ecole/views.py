from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'ecole/index.html')

def contact(request):
    return render(request, 'ecole/contact.html')

def apropos(request):
    return render(request, 'ecole/about.html')