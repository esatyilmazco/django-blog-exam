from re import template
from django.urls import path
from account.views import cikis, profil_guncelle, sifre_degistir, kayit
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('giris', auth_views.LoginView.as_view(
        template_name='pages/giris.html'

    ), name='giris'),
    path('cikis', cikis, name=cikis),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit', kayit, name='kayit')
]
