from django.db import models
from django.contrib.auth.models import User

parcours = (('MISS','MISS'),
            ('MF', 'MF'),
            ('ME', 'ME'),
            )
mention = (('MA', 'Mathematique et Application'),
            ('PC', 'Physique Chimie'),
            ('PA', 'Physique Application'),
            ('SV', 'Science de la vie'),
            )
class inscription(models.Model):
    Carte_etudiant = models.CharField(max_length = 4, verbose_name = u"Carte d'étudiant")
    Nom = models.CharField(max_length = 20)
    Prenom = models.CharField(max_length = 50, verbose_name =  "Prénom")
    Mention = models.CharField(max_length=30, choices = mention, help_text = u"Choisir votre mention")
    Parcour = models.CharField(max_length=30, choices = parcours, help_text = u"Choisir votre parcours")
    mail = models.EmailField(verbose_name = "Email")
    phone = models.CharField(max_length = 10) #min_length?

    def __str__(self):
        return str(self.Nom) + " " +  str(self.Prenom)


class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = u"Choisissez Votre CE: ")
    parcour = models.CharField(choices = parcours, max_length=5,  verbose_name = u"Choisissez Votre Parcours: ")
    avatar = models.ImageField(null = True, blank = True, upload_to='avatars/', default='avatars/student_male_64px.png')

    def __str__(self):
        return str(self.utilisateur) + " " + str(self.parcour)

class Matieres(models.Model):
    CodeMat = models.CharField(primary_key = True, max_length = 10)
    NomMat = models.CharField(max_length = 30)
    Ue = models.CharField(max_length=30)
    Parc = models.ForeignKey(Profil, on_delete = models.CASCADE)

    def __str__(self):
        return self.NomMat

class Note(models.Model):
    NoteUser = models.FloatField(max_length = 10)
    Semestre = models.CharField(max_length = 2)
    Mat = models.ForeignKey(Matieres, on_delete = models.CASCADE)
    Us = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Us) + " " + str(self.NoteUser) + " " + str(self.Mat)

class MoyenneUser(models.Model):
    MoyenneMat = models.FloatField(max_length=10)
    MoyenneTotal = models.FloatField(max_length=10)
    UserMoy = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
