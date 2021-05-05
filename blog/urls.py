from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/', login_user),
    path('logout', logout_user),
    path('signup/', signup),
    path('showuser/', ShowUser),
    path('shownote/', Shownote),
    path('registernote/<str:pk>', RegisterNote, name ='registernote'),
    path('editnote/<str:pk>', EditNote, name ='editnote'),
    path('actualite/', main),
    path('publier/',publier, name='publier'),
    path('note_perso/', note_perso),
    path('password_reset/', 
        auth_view.PasswordResetView.as_view(template_name = 'blog/reset_pwd/reset_password.html'), 
        name = "reset_password"),
    path('password_reset_sent/', 
        auth_view.PasswordResetDoneView.as_view(template_name = 'blog/reset_pwd/password_reset_sent.html'), 
        name = "password_reset_done"),
    path('reset/<uidb64>/<token>', 
        auth_view.PasswordResetConfirmView.as_view(template_name = 'blog/reset_pwd/reset_password_form.html'),
        name = "password_reset_confirm"),
    path('password_complete/',
        auth_view.PasswordResetCompleteView.as_view(template_name = 'blog/reset_pwd/password_complete.html'), 
        name = "password_reset_complete"),
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
    path('fichiers/', fichiers, name='fichiers'),
    path('test/', test),
]