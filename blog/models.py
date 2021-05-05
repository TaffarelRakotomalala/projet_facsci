from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

parcours = (('MISS','MISS'),
            ('MF', 'MF'),
            ('ME', 'ME'),
            )
mentions = (('MA', 'Mathematique et Application'),
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
niveau = (('L1','L1'),
            ('L2','L2'),
            ('L3','L3'),
            ('M1','M1'),
            ('M2','M2'),
            )
desc = (('Cours','Cours'),
        ('TD','TD'),
        ('TP','TP'),
        )

            
class inscription(models.Model):
    Carte_etudiant = models.CharField(primary_key = True, max_length = 4, verbose_name = u"Carte d'étudiant")
    Nom = models.CharField(max_length = 20)
    Prenom = models.CharField(max_length = 50, verbose_name =  "Prénom")
    Mention = models.CharField(max_length=30, choices = mentions, help_text = u"Choisir votre mention")
    Parcour = models.CharField(max_length=30, choices = parcours, help_text = u"Choisir votre parcours")
    mail = models.EmailField(verbose_name = "Email")
    phone = models.CharField(max_length = 10, validators=[RegexValidator(regex='^.{10}$')])

    def __str__(self):
        return str(self.Carte_etudiant)+" "+ str(self.Nom) + " " +  str(self.Prenom)


class Profil(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name = u"Choisissez Votre CE: ")
    parcour = models.CharField(choices = parcours, max_length=5,  verbose_name = u"Choisissez Votre Parcours: ")
    avatar = models.ImageField(null = True, blank = True, upload_to='avatars/', default='avatars/student_male_64px.png')

    class Meta:
        ordering = ['utilisateur',]
    def __str__(self):
        return str(self.utilisateur) + " " + str(self.parcour)


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



class Publication(models.Model):
	pub_titre = models.CharField(max_length=200)
	pub_contenu = models.TextField(null=True,blank=True)
	pub_image = models.FileField(upload_to='files',null=True,blank=True)
	pub_date = models.DateTimeField(auto_now_add=True)


class fichier(models.Model):
    date = models.DateTimeField(auto_now_add=True,verbose_name='Date de ce jour')
    mention = models.CharField(max_length=100,choices=mentions,verbose_name='Mention')
    niveau = models.CharField(max_length=100,choices=niveau,verbose_name='Niveau')
    matiers = models.CharField(max_length=100,verbose_name='Nom des matières')
    desc = models.CharField(max_length=10,choices=desc,verbose_name='Cours ou TD')
    fichiers = models.FileField(upload_to='fichiers/',verbose_name='Nom du fichier')
    util = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="L'utilisateur")

    def __str__(self):
        return str(self.matiers) + " " + str(self.niveau) + " " + str(self.mention)



# Create your models here.
