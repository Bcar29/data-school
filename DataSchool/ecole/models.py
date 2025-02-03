from django.db import models

from DataSchool.settings import AUTH_USER_MODEL
# Create your models here.

class Batiments(models.Model):
    libelle = models.CharField(max_length=32)
    nbre_bloc = models.IntegerField()

    class Meta:
        verbose_name_plural = "Batiments"

    def __str__(self):
        return self.libelle

class Blocs(models.Model):
    libelle = models.CharField(max_length=32)
    nbre_salle = models.IntegerField()
    batiment = models.ForeignKey(Batiments, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Blocs"

    def __str__(self):
        return self.libelle

class Salles(models.Model):
    libelle =models.CharField(max_length=32)
    bloc=models.ForeignKey(Blocs,on_delete=models.CASCADE)
    nbr_place=models.IntegerField()
    disponibilite=models.BooleanField()
    
    class Meta:
        verbose_name_plural = "salles"

    def __str__(self):
        return self.libelle

class Options(models.Model):
    libelle=models.CharField(max_length=32) 

    class Meta:
        verbose_name_plural = "Options"

    def __str__(self):
        return self.libelle  

class Niveaux(models.Model):
    libelle=models.CharField(max_length=32)
    option=models.ForeignKey(Options, on_delete=models.CASCADE)

    class Meta:
       verbose_name_plural = "Niveaux"

    def __str__(self):
        return self.libelle

class Classes(models.Model):
    libelle=models.CharField(max_length=10)
    nbre_place=models.IntegerField()
    niveaux=models.ForeignKey(Niveaux,on_delete=models.CASCADE)

    class Meta:
       verbose_name_plural = "Classes"

    def __str__(self):
        return self.libelle


class Tuteurs(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom=models.CharField(max_length=32)
    prenom=models.CharField(max_length=32)
    tel=models.BigIntegerField()
    email=models.EmailField()
    adress=models.CharField(max_length=32)


    class Meta:
       verbose_name_plural = "Tuteurs"

    def __str__(self):
        return f"Tuteur: {self.nom} {self.prenom}"

class Matieres(models.Model):
    code=models.CharField(max_length=16)
    libelle=models.CharField(max_length=32)

    class Meta:
       verbose_name_plural = "Matieres"

    def __str__(self):
        return self.libelle

GENRE=[
    ("M","Masculin"),
    ("F","Feminin"),

]

class Eleves(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom=models.CharField(max_length=32)
    matricule = models.CharField(max_length=4, editable=False)
    prenom=models.CharField(max_length=32)
    photo=models.ImageField(upload_to="image") 
    sexe=models.CharField(choices=GENRE,max_length=10)
    datenaissance=models.DateField()
    lieunaissance=models.CharField(max_length=50)
    pere=models.CharField(max_length=50)
    mere=models.CharField(max_length=50)
    classe=models.ForeignKey(Classes,on_delete=models.SET_NULL,null=True)
    tuteurs=models.ManyToManyField(Tuteurs)

    class Meta:
       verbose_name_plural = "Eleves"

    def __str__(self):
        return f"Eleve :{self.matricule} {self.nom} {self.prenom}"

    def save(self, *args, **kwargs):
        if not self.matricule : 
            dernier = Eleves.objects.order_by('-id').first()
            if dernier :
                dernier_mat = int(dernier.matricule)
                self.matricule = f"{dernier_mat + 1: 06d}"
            else :
                self.matricule = '0001'
                
        super().save(*args, **kwargs)


class Profs(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    tel = models.BigIntegerField()
    email = models.EmailField()
    adresse = models.CharField(max_length=50)

    class Meta:
       verbose_name_plural = "Profs"

    def __str__(self):
        return f"Prof: {self.nom} {self.prenom}"
    
class Cours(models.Model):
    matiere = models.ForeignKey(Matieres, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveaux,on_delete=models.CASCADE)
    prof = models.ForeignKey(Profs,on_delete=models.CASCADE)
    coef = models.IntegerField()
    option = models.ForeignKey(Options, on_delete=models.CASCADE)

    class Meta:
       verbose_name_plural = "Cours"

    def __str__(self):
        return f"Matiere: {self.matiere} {self.niveau}"

JOURS = [("Lu","Lundi"),("Ma","Mardi"),("Mr","Mercredi"),("Je","Jeudi"),("Ve","Vendredi"),("Sa","Samedi")]

class Emplois(models.Model):
    jour = models.CharField(choices=JOURS,max_length=10)
    classe = models.ForeignKey(Classes , on_delete=models.CASCADE)
    salle = models.ForeignKey(Salles , on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours , on_delete=models.CASCADE)
    prof = models.ForeignKey(Profs , on_delete=models.CASCADE)
    heuredebut = models.TimeField()
    heurefin = models.TimeField()

    class Meta:
       verbose_name_plural = "Emplois"

    def __str__(self):
        return self.classe
 
class Seances(models.Model):
    heuredebut=models.TimeField()
    heurefin=models.TimeField()
    cours=models.ForeignKey(Cours, on_delete=models.CASCADE)
    classe=models.ForeignKey(Classes, on_delete=models.CASCADE)
    salle=models.ForeignKey(Salles, on_delete=models.CASCADE)
    prof=models.ForeignKey(Profs, on_delete=models.CASCADE)
    nombreEleve=models.IntegerField()
    eleve = models.ManyToManyField(Eleves,through='EleveSeances')

    class Meta:
       verbose_name_plural = "Seances"

    def __str__(self):
        return f"{self.classe} {self.cours}"

class EleveSeances(models.Model):
    eleve = models.ForeignKey(Eleves,on_delete=models.CASCADE)
    seance = models.ForeignKey(Seances,on_delete=models.CASCADE)
    jour = models.ForeignKey(Emplois,on_delete=models.CASCADE)
    presence = models.BooleanField()



class Evaluation(models.Model):
    classe = models.ForeignKey(Classes,on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours,on_delete=models.CASCADE)
    nbreEleve = models.IntegerField()
    date = models.DateField()
    eleve = models.ManyToManyField(Eleves)

    class Meta:
       verbose_name_plural = "Evaluations"

    def __str__(self):
        return f"Evaluation: {self.classe} {self.cours}"

class Notes(models.Model):
    eleve = models.ForeignKey(Eleves,on_delete=models.CASCADE)
    prof = models.ForeignKey(Profs,on_delete=models.SET_NULL,null=True)
    cours = models.ForeignKey(Cours,on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation,on_delete=models.CASCADE)
    note1 = models.FloatField()
    note2 = models.FloatField()
    note3 = models.FloatField()
    moy = models.FloatField()

    class Meta:
       verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.eleve} {self.moy}"
    
    def save(self, *args, **kwargs):
        notes = [self.note1, self.note2, self.note3]
        n = [i for i in notes if i]
        self.moy = sum(n)/len(n)

        super().save(*args, **kwargs)

MOIS = [("Oct","Octobre"),("Nov","Novembre"),("Dec","Decembre"),("Jan","Janvier"),("Fev","Fevrier"),("Mar","Mars"),("Avr","Avril"),("Mai","Mai"),("Juin","Juin"),("Juil","Juillet")]

class Mensualites(models.Model):
    eleve = models.ForeignKey(Eleves,on_delete=models.CASCADE)
    montant = models.FloatField()
    mois = models.CharField(choices=MOIS,max_length=20)
    moyenpai = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
       verbose_name_plural = "Mensualites"

    def __str__(self):
        return f"Mensualites: {self.eleve} {self.mois} {self.montant}"

TYPES = [("Ins","Inscription"),("Reins","Reinscription"),("Mens","Mensualite")]

class Paiements(models.Model):
    eleve = models.ForeignKey(Eleves,on_delete=models.CASCADE)
    types = models.CharField(choices=TYPES,max_length=20)
    montant = models.FloatField()
    modepaie = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
       verbose_name_plural = "Paiements"

    def __str__(self):
        return f"Paiement: {self.eleve} {self.montant}"

class Inscriptions(models.Model):
    eleve = models.ForeignKey(Eleves,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
       verbose_name_plural = "Inscriptions"

    def __str__(self):
        return f"Inscription: {self.eleve} {self.date} "










    


























