from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def hafatra(request):
    messages.add_message(request, messages.INFO, u'Pour Info')
    messages.success(request, u'Inscription avec Succès')
    messages.warning(request, u"Pour l'attention")
    messages.error(request, u"Pour l'erreur")



def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(signup1)
    return render(request, 'blog/signup.html', locals())

def signup1(request):
    sauvegarde = False
    form = UserForm1()
    if request.method == 'POST':
        form = UserForm1(request.POST)
        if form.is_valid:
            form.save()
            hafatra(request)
            sauvegarde = True
            return render(request, 'blog/signup1.html', locals())
    return render(request, 'blog/signup1.html', locals())



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        etudiant = authenticate(request, username = username, password = password)
        if etudiant is not None:
            login(request, etudiant)
            return redirect(main)
        else:
            hafatra(request)
    return render(request, 'blog/facsci.html')

def logout_user(request):
    logout(request)
    return redirect(login_user)



@login_required(login_url = '../login/')
def main(request):
    return render(request, 'blog/main.html')

@login_required(login_url = '../login/')
def note_perso(request):
    inst = request.user.profil
    form = UserForm1(instance = inst)
    if request.method == "POST":
        form = UserForm1(request.POST, request.FILES, instance = inst)
        if form.is_valid:
            form.save()
            return redirect(note_perso)
    return render(request, 'blog/personnel/note.html', locals())

@login_required(login_url = '../login/')
def afficherForum(request):
	return render(request, 'blog/forum/forum_liste.html')


@login_required(login_url = '../login/')
def nouveauForum(request):
	formNouveau = forumForm(request.POST or None)
	if formNouveau.is_valid():
		mention=formNouveau.cleaned_data['mention']
		message=formNouveau.cleaned_data['message']
		sujet=formNouveau.cleaned_data['sujet']
		envoi=True
	return render(request, 'blog/forum/forum_nouveau.html', locals())


@login_required(login_url = '../login/')
def reponseForum(request):
	formReponse = reponseForm(request.POST or None)
	if formReponse.is_valid():
		txtReponse=formReponse.cleaned_data['reponse']
		envoi=True
	return render(request, 'blog/forum/forum_reponse.html', locals())

@login_required(login_url = '../login/')
def notification(request):
	return render(request, 'blog/notification.html')

@login_required(login_url = '../login/')
def fichiers(request):
	return render(request, 'blog/fichiers.html')

#--------------- M.I.S.S ----------------
@login_required(login_url = '../login/')
def missl1(request):
    return render(request, 'blog/math/miss/missl1.html')

@login_required(login_url = '../login/')
def missl2(request):
    return render(request, 'blog/math/miss/missl2.html')

@login_required(login_url = '../login/')
def missl3(request):
    return render(request, 'blog/math/miss/missl3.html')

@login_required(login_url = '../login/')
def missm1(request):
    return render(request, 'blog/math/miss/missm1.html')

@login_required(login_url = '../login/')
def missm2(request):
    return render(request, 'blog/math/miss/missm2.html')


#------------ M.E --------------
@login_required(login_url = '../login/')
def mel1(request):
    return render(request, 'blog/math/me/mel1.html')

@login_required(login_url = '../login/')
def mel2(request):
    return render(request, 'blog/math/me/mel2.html')

@login_required(login_url = '../login/')
def mel3(request):
    return render(request, 'blog/math/me/mel3.html')

@login_required(login_url = '../login/')
def mem1(request):
    return render(request, 'blog/math/me/mem1.html')

@login_required(login_url = '../login/')
def mem2(request):
    return render(request, 'blog/math/me/mem2.html')

# --------- M.F ------------

@login_required(login_url = '../login/')
def mfl1(request):
    return render(request, 'blog/math/mf/mfl1.html')

@login_required(login_url = '../login/')
def mfl2(request):
    return render(request, 'blog/math/mf/mfl2.html')

@login_required(login_url = '../login/')
def mfl3(request):
    return render(request, 'blog/math/mf/mfl3.html')

@login_required(login_url = '../login/')
def mfm1(request):
    return render(request, 'blog/math/mf/mfm1.html')

@login_required(login_url = '../login/')
def mfm2(request):
    return render(request, 'blog/math/mf/mfm2.html')

#----------- B.D ---------------

@login_required(login_url = '../login/')
def bdl1(request):
    return render(request, 'blog/sv/bd/bdl1.html')

@login_required(login_url = '../login/')
def bdl2(request):
    return render(request, 'blog/sv/bd/bdl2.html')

@login_required(login_url = '../login/')
def bdl3(request):
    return render(request, 'blog/sv/bd/bdl3.html')

@login_required(login_url = '../login/')
def bdm1(request):
    return render(request, 'blog/sv/bd/bdm1.html')

@login_required(login_url = '../login/')
def bdm2(request):
    return render(request, 'blog/sv/bd/bdm2.html')

# -------------- B.M --------------

@login_required(login_url = '../login/')
def bml1(request):
    return render(request, 'blog/sv/bm/bml1.html')

@login_required(login_url = '../login/')
def bml2(request):
    return render(request, 'blog/sv/bm/bml2.html')

@login_required(login_url = '../login/')
def bml3(request):
    return render(request, 'blog/sv/bm/bml3.html')

@login_required(login_url = '../login/')
def bmm1(request):
    return render(request, 'blog/sv/bm/bmm1.html')

@login_required(login_url = '../login/')
def bmm2(request):
    return render(request, 'blog/sv/bm/bmm2.html')

# ------------- CAP -------------------
@login_required(login_url = '../login/')
def capl1(request):
    return render(request, 'blog/pa/cap/capl1.html')

@login_required(login_url = '../login/')
def capl2(request):
    return render(request, 'blog/pa/cap/capl2.html')

@login_required(login_url = '../login/')
def capl3(request):
    return render(request, 'blog/pa/cap/capl3.html')

@login_required(login_url = '../login/')
def capm1(request):
    return render(request, 'blog/pa/cap/capm1.html')

@login_required(login_url = '../login/')
def capm2(request):
    return render(request, 'blog/pa/cap/capm2.html')

#---------------- EA2I ----------------

@login_required(login_url = '../login/')
def ea2il1(request):
    return render(request, 'blog/pa/ea2i/ea2il1.html')

@login_required(login_url = '../login/')
def ea2il2(request):
    return render(request, 'blog/pa/ea2i/ea2il2.html')

@login_required(login_url = '../login/')
def ea2il3(request):
    return render(request, 'blog/pa/ea2i/ea2il3.html')

@login_required(login_url = '../login/')
def ea2im1(request):
    return render(request, 'blog/pa/ea2i/ea2im1.html')

@login_required(login_url = '../login/')
def ea2im2(request):
    return render(request, 'blog/pa/ea2i/ea2im2.html')

#-------------- MET --------------

@login_required(login_url = '../login/')
def metl1(request):
    return render(request, 'blog/pa/met/metl1.html')

@login_required(login_url = '../login/')
def metl2(request):
    return render(request, 'blog/pa/met/metl2.html')

@login_required(login_url = '../login/')
def metl3(request):
    return render(request, 'blog/pa/met/metl3.html')

@login_required(login_url = '../login/')
def metm1(request):
    return render(request, 'blog/pa/met/metm1.html')

@login_required(login_url = '../login/')
def metm2(request):
    return render(request, 'blog/pa/met/metm2.html')

@login_required(login_url = '../login/')
def test(request):
    return render(request, 'blog/test.html')

