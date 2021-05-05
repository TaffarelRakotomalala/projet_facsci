from django.contrib import admin
from blog.models import *


class InscriptionAdmin(admin.ModelAdmin):
    ordering = ('Carte_etudiant',)

class Note_Admin(admin.ModelAdmin):
    list_display = ('Us', 'Nom_Mat', 'Note',)
    list_filter = ('Nom_UE','Nom_Mat','Semestre','Us')
    search_fields = ('Us',)
    ordering = ('Us',)

admin.site.register(Profil)
admin.site.register(Note_User, Note_Admin)
# admin.site.register(Note)
# admin.site.register(MoyenneUser)
admin.site.register(inscription, InscriptionAdmin)
admin.site.register(Publication)
admin.site.register(fichier)

# Register your models here.
