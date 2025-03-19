from django import forms
from ecole.models import Tuteurs, Eleves, Profs

class TuteursForm(forms.ModelForm):
    class Meta:
        model = Tuteurs
        fields = ['nom', 'prenom',  'tel']  # Les champs à inclure dans le formulaire
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ElevesForm(forms.ModelForm):
    class Meta:
        model = Eleves
        fields = ['nom', 'prenom', 'photo', 'sexe', 'lieunaissance', 'pere', 'mere']
        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'matricule': 'Matricule',
            'photo': 'Photo de profil',
            'sexe': 'Sexe',
            'datenaissance': 'Date de naissance',
            'lieunaissance': 'Lieu de naissance',
            'pere': 'Nom du père',
            'mere': 'Nom de la mère',
            'classe': 'Classe',
        }
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            # 'matricule': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'sexe': forms.Select(choices=[('M', 'Masculin'), ('F', 'Féminin')], attrs={'class': 'form-select'}),
            # 'datenaissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieunaissance': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le lieu de naissance'}),
            'pere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du père'}),
            'mere': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la mère'}),
            # 'classe': forms.Select(attrs={'class': 'form-select', 'readonly'}),
        }


class ProfsForm(forms.ModelForm):
    class Meta:
        model = Profs
        fields = ['nom', 'prenom', 'tel', 'addresse']

        labels = {
            'nom': 'Nom',
            'prenom': 'Prénom',
            'tel': 'Téléphone',
            'addresse': 'Addresse'
        }

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'addresse': forms.Select(attrs={'class': 'form-controle'}),
        }