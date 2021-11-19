from django.urls import path
from account.views import cikis


urlpatterns = [
    path('cikis',cikis,name=cikis)
]
