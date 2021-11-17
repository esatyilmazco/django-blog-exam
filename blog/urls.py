
from django.urls import path,include
from blog.views import iletisim,anasayfa,kategori

urlpatterns = [
    path('',anasayfa,name='anasayfa'),
    path('iletisim',iletisim,name='iletisim'),
    path('kategori/<slug:kategoriSlug>',kategori,name='kategori')
]