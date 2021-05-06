from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.http import HttpResponse, Http404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def hafatra(request):
    messages.add_message(request, messages.INFO, u'Pour Info')
    messages.success(request, u'Inscription avec Succès')
    messages.warning(request, u"Pour l'attention")
    messages.error(request, u"Pour l'erreur")



# def signup(request):
#     form = UserForm()
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect(signup1)
#     return render(request, 'blog/signup.html', locals())


#-------- Inscription ----------
def signup(request):
    sauvegarde = False
    erreur = False
    form = InscriptionForm()
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        try:
            if form.is_valid:
                form.save()
                hafatra(request)
                sauvegarde = True
                return render(request, 'blog/signup.html', locals())
        except ValueError:
            erreur = True
            return render(request, 'blog/signup.html', locals())
    return render(request, 'blog/signup.html', locals())





#--------- login ---------------
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

#----------Pour l'admin ------------
# ---------- Liste des Utilisateurs
@login_required(login_url = '../login/')
def ShowUser(request):
    if request.user.is_staff:
        userliste = User.objects.filter(is_staff = False).order_by('username')
        if request.method == "POST":
            rech = request.POST['rech']
            userliste = User.objects.filter(username__icontains = f"{rech}")
            return render(request, "blog/admin/showuser.html", locals())
        else:
            return render(request, "blog/admin/showuser.html", locals())
    else:
        return redirect(main)
# -----------------------------------

#---------- Registre Note -----------
@login_required(login_url = '../showuser/')
def RegisterNote(request, pk):
    if request.user.is_superuser:
        erreur = False
        success = False
        form = EnregistrerNote()
        if request.method == 'POST':
            note = Note_User()
            note.Us = User.objects.get(username = pk)
            form = EnregistrerNote(request.POST, instance = note)
            try:
                if form.is_valid:
                    form.save()
                    success = True
                    return render(request, 'blog/admin/registernote.html', locals())
            except:
                erreur = True
                return render(request, 'blog/admin/registernote.html', locals())
        return render(request, 'blog/admin/registernote.html', locals())
    else:
        return redirect(ShowUser)
# -----------------------------------

# ------- Modification Note ------------
@login_required(login_url = '../login/')
def Shownote(request):
    if request.user.is_staff:
        user_notes = Note_User.objects.all().order_by('Us', 'Semestre')
        if request.method == "POST":
            rech = request.POST['rech']
            user_notes = Note_User.objects.filter(Us__username__icontains = f"{rech}").order_by('Semestre')
            return render(request, 'blog/admin/shownote.html', locals())
        else:
            return render(request, 'blog/admin/shownote.html', locals())
    else:
        return redirect(main)

@login_required(login_url = '../login/')
def EditNote(request, pk):
    if request.user.is_superuser:
        erreur = False
        success = False
        note_user = Note_User.objects.get(id = pk)
        form = EnregistrerNote(instance = note_user)
        if request.method == 'POST':
            form = EnregistrerNote(request.POST, instance = note_user)
            if form.is_valid:
                form.save()
                return redirect(Shownote)
        else:
            return render(request, 'blog/admin/editnote.html', locals())
    else:
        return redirect(Shownote)
# ----------------------------------------------------------------


# ------------------Actualité-----------------
@login_required(login_url = '../login/')
def main(request):
    publications = Publication.objects.all()
    return render(request, 'blog/main.html', {'publications': publications})

#-------- Publication ---------------
@login_required(login_url = '../login/')
def publier(request):
    if request.user.is_staff:
        form = publierForm()
        publications = Publication.objects.all()
        if request.method=='POST':
            form = publierForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                return render(request,'blog/main.html', {'publications': publications})
        return render(request, 'blog/publication.html', locals())
    else:
        return redirect(main)


@login_required(login_url = '../login/')
def note_perso(request):
    util = request.user.username
    inst = request.user.profil
    form = UserForm1(instance = inst)
    if request.method == "POST":
        form = UserForm1(request.POST, request.FILES, instance = inst)
        if form.is_valid:
            form.save()
            return redirect(note_perso)
    #affichage Note
    # --------- Moyenne par UE -----------
    N = ()
    P = []
    u_e = []
    Moy_UE = 0
    validation = "Non validé"
    resultat = []
    S = []
    sem = Note_User.objects.filter(Us__username = util)
    for s in sem:
        if s.Semestre not in S:
            S.append(s.Semestre)
    for semestre in S:
        ue = Note_User.objects.filter(Us__username = util, Semestre = semestre)
        for i in ue:
            if i.Nom_UE not in u_e:
                u_e.append(i.Nom_UE)
        for i in u_e:
            u = Note_User.objects.filter(Nom_UE = i, Us__username = util, Semestre = semestre)
            for j in u:
                N = (i, j.Note, j.Poids_Mat)
                P.append(N)

            for k in range(len(P)):
                if P[k][0] == i:
                    Moy_UE += P[k][1]*P[k][2]
                    if Moy_UE >=10:
                        validation = "Validé"
            resultat.append((semestre, i, f"{Moy_UE:.2f}", validation))
            Moy_UE = 0
            u_e = []
            P = []
            validation = "Non validé"
    noty = Note_User.objects.filter(Us__username = util).order_by("Semestre")
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
def fichiers(request):
    u = request.user.username
    f = fichier.objects.all()
    form = fichierForm()
    if request.method=='POST':
        fch = fichier()
        fch.util = User.objects.get(username = u)
        form = fichierForm(request.POST, request.FILES, instance = fch)
        if form.is_valid():
            form.save()
            return render(request,'blog/fichiers.html', locals())
    return render(request,'blog/fichiers.html', locals())

@login_required(login_url = '../login/')
def test(request):
    util = request.user.username
    noty = Note_User.objects.filter(Us__username__contains = util).order_by("Semestre")
    return render(request, 'blog/test.html', locals())
