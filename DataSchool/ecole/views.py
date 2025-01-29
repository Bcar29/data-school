from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'ecole/index.html')



def contact(request):
    return render(request, 'ecole/contact.html')

def about(request):
    return render(request, 'ecole/about.html')
