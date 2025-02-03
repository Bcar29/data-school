from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Batiments)
class BatimentAdmin(admin.ModelAdmin):
    list_display = ("libelle","nbre_bloc")

@admin.register(Blocs)
class BlocsAdmin(admin.ModelAdmin):
    list_display = ("libelle","nbre_salle","batiment")

@admin.register(Salles)
class SallesAdmin(admin.ModelAdmin):
    list_display = ("libelle","nbr_place","disponibilite","bloc")

@admin.register(Options)
class optionsAdmin(admin.ModelAdmin):
    list_display = ("libelle",)

@admin.register(Niveaux)
class NiveauxAdmin(admin.ModelAdmin):
    list_display = ("libelle","option",)

@admin.register(Classes)
class ClassesAdmin(admin.ModelAdmin):
    list_display = ("libelle","nbre_place","niveaux")
    
@admin.register(Eleves)
class ElevesAdmin(admin.ModelAdmin):
    list_display = ("nom","prenom", "matricule", "sexe", "classe")


@admin.register(Profs)
class ProfsAdmin(admin.ModelAdmin):
    list_display = ("user", "nom","prenom", "tel", "email", "addresse")

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ("matiere", "niveau", "prof", "coef", "option")

@admin.register(Emplois)
class EmploisAdmin(admin.ModelAdmin):
    list_display = ("jour", "heuredebut", "heurefin", "classe", "salle", "cours", "prof")

@admin.register(Seances)
class SeancesAdmin(admin.ModelAdmin):
    list_display = ("heuredebut", "heurefin", "cours", "classe", "salle", "prof", "nombreEleve")

@admin.register(Evaluations)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ("classe", "cours", "nbreEleve", "date")


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ("eleve", "prof", "cours", "evaluation", "note1", "note2", "note3", "moy")

@admin.register(Mensualites)
class MensualitesAdmin(admin.ModelAdmin):
    list_display = ("eleve", "montant", "mois", "date")

 