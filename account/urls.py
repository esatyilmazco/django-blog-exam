from django.urls import path
from account.views import cikis, profil_guncelle, sifre_degistir, kayit


urlpatterns = [
    path('cikis', cikis, name=cikis),
    path('sifre-degistir', sifre_degistir, name='sifre-degistir'),
    path('profil-guncelle', profil_guncelle, name='profil-guncelle'),
    path('kayit', kayit, name='kayit')
]
