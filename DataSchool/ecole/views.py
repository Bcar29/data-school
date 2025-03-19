from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import *
from .forms import *

# Create your views here.
# ---------------------------------------------------LA PAGE D'ACCUEIL--------------------------------------------------#
def accueil(request):
    
    return render(request, 'ecole/index.html')

# --------------------------------------------------LA PAGE DE CONTACT--------------------------------------------------#
def contact(request):
    return render(request, 'ecole/contact.html')

# ---------------------------------------------------LA PAGE D'APROPOS--------------------------------------------------#
def apropos(request):
    return render(request, 'ecole/about.html')


# ---------------------------------------------------L'ESPACE ELEVES----------------------------------------------------#
class Espace_eleve(UpdateView):
    model = Eleves
    template_name = "ecole/espace_eleve.html"
    form_class = ElevesForm

    success_url = reverse_lazy('ecole:eleve')

    def get_object(self, queryset = None):
        return self.request.user.eleves

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eleve'] = self.get_object()  # Ajouter l'élève au contexte

        return context


# ----------------------------------------L'ASSOCIATION D'UN ENFANT A UN PARENT-----------------------------------------#
def parentAdd(request):
    parent = request.user.tuteurs  # Assume que l'utilisateur a un tuteur associé
    if request.method == "POST":
        mat = request.POST.get("matricule")
        
        # Récupérer l'élève en fonction du matricule
        try:
            eleve = get_object_or_404(Eleves, matricule=mat)
             
            # Ajouter l'élève à l'enfant du parent
            parent.enfant.add(eleve)
            messages.success(request, "L'élève a été ajouté avec succès.")
        except Exception as e:
            messages.error(request, f"Erreur lors de l'ajout de l'élève : {str(e)}")

    return redirect('ecole:parent')


# ---------------------------------------------------L'ESPACE PARENTS----------------------------------------------------#
class Espace_parent(UpdateView):
    model = Tuteurs
    template_name = "ecole/espace_parent.html"
    form_class = TuteursForm

    success_url = reverse_lazy('ecole:parent')

    def get_object(self, queryset = None):
        """
        Cette méthode permet de récupérer l'objet à mettre à jour.
        On retourne ici l'objet. `Tuteurs` associé à l'utilisateur actuellement connecté.
        """
        return self.request.user.tuteurs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        enfant = self.request.user.tuteurs.enfant.all()
        context['enfants'] = enfant
        # context['emplois'] = enfant.classe.emplois_set.all()

        return context
        

# ---------------------------------------------------L'ESPACE PROFESSEURS-----------------------------------------------#
class espace_prof(UpdateView):
    model = Profs
    template_name = "ecole/espace_prof.html"
    form_class = ProfsForm

    success_url = reverse_lazy('ecole:prof')

    def get_object(self, queryset = None):
        """
        Cette méthode permet de récupérer l'objet à mettre à jour.
        On retourne ici l'objet. `Tuteurs` associé à l'utilisateur actuellement connecté.
        """
        return self.request.user.profs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emplois'] = self.request.user.profs.emplois_set.all()
        context['matieres'] = self.request.user.profs.matieres_set.all()
        
        
        return context
