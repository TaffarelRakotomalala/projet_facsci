from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

parcours = (('MISS','MISS'),
            ('MF', 'MF'),
            ('ME', 'ME'),
            )
mention = (('MA', 'Mathematique et Application'),
            ('PC', 'Physique Chimie'),
            ('PA', 'Physique Application'),
            ('SV', 'Science de la vie'),
            )
semestre = (('S1','S1'),
            ('S2','S2'),
            ('S3','S3'),
            ('S4','S4'),
            ('S5','S5'),
            ('S6','S6'),
            ('S7','S7'),
            ('S8','S8'),
            ('S9','S9'),
            ('S10','S10'),
            )
            
class inscription(models.Model):
    Carte_etudiant = models.CharField(primary_key = True, max_length = 4, verbose_name = u"Carte d'étudiant")
    Nom = models.CharField(max_length = 20)
    Prenom = models.CharField(max_length = 50, verbose_name =  "Prénom")
    Mention = models.CharField(max_length=30, choices = mention, help_text = u"Choisir votre mention")
    Parcour = models.CharField(max_length=30, choices = parcours, help_text = u"Choisir votre parcours")
    mail = models.EmailField(verbose_name = "Email")
    phone = models.CharField(max_length = 10, validators=[RegexValidator(regex='^.{10}$')])
    #ouiounon = models.BooleanField()

    def __str__(self):
        return str(self.Carte_etudiant)+""+ str(self.Nom) + " " +  str(self.Prenom)


class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = u"Choisissez Votre CE: ")
    parcour = models.CharField(choices = parcours, max_length=5,  verbose_name = u"Choisissez Votre Parcours: ")
    avatar = models.ImageField(null = True, blank = True, upload_to='avatars/', default='avatars/student_male_64px.png')

    class Meta:
        ordering = ['utilisateur',]
    def __str__(self):
        return str(self.utilisateur) + " " + str(self.parcour)
# class Unite_Ens(models.Model):
#     Nom_UE = models.CharField(max_length = 20)
#     Semestre = models.CharField(max_length=3, choices = semestre)
#     Parc = models.ForeignKey(Profil, on_delete = models.CASCADE, verbose_name="Parcour")

#     def __str__(self):
#         return str(self.Nom_UE)+""+str(self.Parc)
    
# class Matieres(models.Model):
#     NomMat = models.CharField(max_length = 30)
#     Ue = models.ForeignKey(Unite_Ens, on_delete=models.CASCADE, verbose_name="Unité d'enseignement")

#     def __str__(self):
#         return self.NomMat

class Note_User(models.Model):
    Semestre = models.CharField(max_length=3, choices = semestre, null=True)
    Nom_UE = models.CharField(max_length = 20, verbose_name = "Unité d'enseignement",null=True)
    Nom_Mat = models.CharField(max_length = 30, verbose_name = "Matieres",null=True)
    Note = models.FloatField(max_length = 10, verbose_name = "Note",null=True)
    Poids_Mat = models.FloatField(max_length = 10, verbose_name = "Poids Matieres", null = True)
    Validation_UE = models.BooleanField(default = False)
    Validation_Semestre = models.BooleanField(default = False)
    Us = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="L'étudiant")
    
    

    def __str__(self):
        return str(self.Us) + " " + str(self.Nom_Mat) + " " + str(self.Note)


# class MoyenneUser(models.Model):
#     MoyenneMat = models.FloatField(max_length=10)
#     MoyenneTotal = models.FloatField(max_length=10)
#     UserMoy = models.ForeignKey(User, on_delete=models.CASCADE)


# Create your models here.
