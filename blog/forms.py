from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

attrEmail={'type':'email','class':'form-control','id':'email'}
attrPassw={'type':'password','class':'form-control','id':'pwd'}
attrText={'type':'text','class':'form-control','id':'usr'}
attrCombo={'class':'form-control','id':'sel1'}
attrCE = {'class':'form-control', 'placeholder':'1234', 'disabled':'disabled'}
attrNOM = {'class':'form-control', 'placeholder':'RAKOTOMALALA', 'disabled':'disabled'}
attrPRENOM = {'class':'form-control', 'placeholder':'Harisetra Taffarel', 'disabled':'disabled'}
attrParcour = {'class':'form-control', 'placeholder':'MISS', 'disabled':'disabled'}
attrMail = {'class':'form-control', 'placeholder':'taffarelrakotomalala@gmail.com'}
attrFichier = {'class':'form-control',}

 
class forumForm(forms.Form):
	attr={'class':'form-control'}
	attrText['placeholder']='Sujet de forum'
	CHOICES=[('1','Toute'),('2','Mathématiques'),('3','Physique/Chimie'),('4','Science de la Vie')]
	mention = forms.ChoiceField(choices=CHOICES,widget=forms.Select(attrs=attrCombo))
	sujet = forms.CharField(max_length=100,widget=forms.TextInput(attrs=attrText))
	attrText['placeholder']='Votre forum'
	message = forms.CharField(widget=forms.Textarea(attrs=attrText))

class reponseForm(forms.Form):
	attrText['placeholder']='Votre reponse'
	reponse = forms.CharField(widget=forms.Textarea(attrs=attrText))

# class profilForm(forms.Form):
# 	class Meta:
# 		model = Profil
# 		fields = ['parcour', 'avatar']


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']

		widgets = {
            'username': forms.TextInput(attrs={'placeholder': "Entrer votre carte d'étudiant", 'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'placeholder' : "Entrer votre Nom", 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'placeholder' : "Entrer votre Prénom", 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder' : "Entrer votre email", 'class': 'form-control'}),
        }
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["password1"].widget.attrs['placeholder'] = "Entrer Votre mot de passe"
		self.fields["password1"].widget.attrs['class'] = "form-control"
		self.fields["password2"].widget.attrs['placeholder'] = 'Confirmer votre mot de passe'
		self.fields["password2"].widget.attrs['class'] = "form-control"

class UserForm1(ModelForm):
	class Meta:
		model = Profil
		fields = ['avatar']

		widgets = {
			'avatar':forms.FileInput(attrs={'class': 'form-control'})
        }



        
