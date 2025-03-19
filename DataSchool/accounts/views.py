from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from ecole.models import Classes, Niveaux,Eleves,Tuteurs, Options
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from DataSchool import settings
from django.contrib import messages
from .forms import *

# print(Classes,Niveaux)
# Create your views here.
User = get_user_model()

# pour identifier les classe par exemple : 10em Année B
CLASSE = ["A", "B", "C", "D", "E", "F", "G", "H"]

def Inscription(request):
    Nivaux = Niveaux.objects.all()
    options = Options.objects.all()

    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'student':
            print(user_type)
            prenom = request.POST.get('prenom')
            nom = request.POST.get('nom')
            niveau = request.POST.get('niveau')
            genre = request.POST.get('genre')
            date_naissance=request.POST.get('dateNaissance')
            lieu_naissance = request.POST.get('lieuNaissance')
            prenom_pere = request.POST.get('prenomPere')
            prenom_mere = request.POST.get('prenomMere')
            nom_mere = request.POST.get('nomMere')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_confirmation = request.POST.get('passwordConfirmation')
        
            niv = get_object_or_404(Niveaux, pk=int(niveau))
            cla = niv.classes_set.last() 

            if len(cla.eleves_set.all()) == cla.nbre_place:
               cla = Classes.objects.create(libelle = niv.libelle + " " + CLASSE[len(niv.classes_set.all())], nbre_place = cla.nbre_place, niveaux=niv)

            pere= prenom_pere + " " + nom 
            mere = prenom_mere + " " + nom_mere
            if password and password == password_confirmation:
                user= User.objects.create_user(email=email, password=password)
                # login(request,user)
                el = Eleves.objects.create(user=user,nom=nom,prenom=prenom,sexe=genre,datenaissance=date_naissance,lieunaissance=lieu_naissance,pere = pere,mere = mere, classe=cla)
                mat = el.matricule
                classe = el.classe
                return redirect('ecole:home')
            
            el = Eleves.objects.create(nom=nom,prenom=prenom,sexe=genre,datenaissance=date_naissance,lieunaissance=lieu_naissance,pere = pere,mere = mere, classe=cla)
            mat = el.matricule
            classe = el.classe
            return redirect('ecole:home') 


        elif user_type == 'parent':
            prenom = request.POST.get('p_prenom')
            nom = request.POST.get('p_nom')
            adresses = request.POST.get('p_adresse')
            email = request.POST.get('p_email')
            telephone = request.POST.get('p_telephone')
            password = request.POST.get('p_password')
            password_confirmation = request.POST.get('p_passwordConfirmation')
            if password == password_confirmation:
                user= User.objects.create_user(email=email, password=password)
                Tuteurs.objects.create(user=user, nom=nom, prenom=prenom, tel=telephone, adress=adresses)
                login(request, user)
                return redirect('ecole:home')



    return render(request, 'accounts/register.html', {'opt':options, 'niveau': Nivaux})


def Connexion(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
            return redirect("ecole:home")
    
    return render(request, 'accounts/login.html')


def Deconnexion(request):
    logout(request)
    return redirect("ecole:home")

#-----------------------------------------changement de mot de passe---------------------------------------------#
def changePassword(request):
    if request.method == "POST":
        old_pwd = request.POST.get('ancien')
        new_pwd1 = request.POST.get('new1')
        new_pwd2 = request.POST.get('new2')
        if new_pwd1 == new_pwd2:
            if request.user.check_password(old_pwd):
                request.user.set_password(new_pwd1)
                request.user.save()
                update_session_auth_hash(request, request.user)
                return redirect('ecole:home')

        
    # return render(request, 'accounts/changePassword.html')


# -------------------------------------------------demande de reinitialisation de password-------------------------#
class password_reset(PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    password_reset_form = ResetForm
    email_template_name = 'accounts/password_reset_email.html'
    from_email = settings.DEFAULT_FROM_EMAIL
    
    success_url = reverse_lazy("ecole:home")

    def form_valid(self, form):
        messages.info(self.request, "Verifiez votre boite email pour confirmez la reinitialisation.")
        return super().form_valid(form)

# ------------------------------------------------reinitialisation de password---------------------------------------#
class password_reset_confirm(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    form_class = ResetConfirmForm
    success_url = reverse_lazy("ecole:home")
    


    def form_valid(self, form):
        messages.success(self.request, "Votre mot de passe a été modifié avec succès.")
        return super().form_valid(form)