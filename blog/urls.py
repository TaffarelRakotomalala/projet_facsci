from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login_user),
    path('logout', logout_user),
    path('signup/', signup),
    path('signup1/', signup1),
    path('actualite/', main),
    path('note_perso/', note_perso),
    path('forum/',afficherForum),
    path('forum/nouveau/',nouveauForum,name='forum'),
    path('forum/reponse/',reponseForum,name='reponse'),
    path('notification/',notification),
    path('fichiers/', fichiers),
    path('missl1/', missl1),
    path('missl2/', missl2),
    path('missl3/', missl3),
    path('missm1/', missm1),
    path('missm2/', missm2),
    path('mel1/', mel1),
    path('mel2/', mel2),
    path('mel3/', mel3),
    path('mem1/', mem1),
    path('mem2/', mem2),
    path('mfl1/', mfl1),
    path('mfl2/', mfl2),
    path('mfl3/', mfl3),
    path('mfm1/', mfm1),
    path('mfm2/', mfm2),
    path('bdl1/', bdl1),
    path('bdl2/', bdl2),
    path('bdl3/', bdl3),
    path('bdm1/', bdm1),
    path('bdm2/', bdm2),
    path('bml1/', bml1),
    path('bml2/', bml2),
    path('bml3/', bml3),
    path('bmm1/', bmm1),
    path('bmm2/', bmm2),
    path('capl1/', capl1),
    path('capl2/', capl2),
    path('capl3/', capl3),
    path('capm1/', capm1),
    path('capm2/', capm2),
    path('ea2il1/', ea2il1),
    path('ea2il2/', ea2il2),
    path('ea2il3/', ea2il3),
    path('ea2im1/', ea2im1),
    path('ea2im2/', ea2im2),
    path('metl1/', metl1),
    path('metl2/', metl2),
    path('metl3/', metl3),
    path('metm1/', metm1),
    path('metm2/', metm2),
    path('test/', test),
]