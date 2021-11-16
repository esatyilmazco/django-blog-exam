from django.contrib import admin
from blog.models import(
    KategoriModel,Yazilar,YorumModel,IletisimModel
    )
# Register your models here.
admin.site.register(KategoriModel)

@admin.register(Yazilar)
class YazilarAdmin(admin.ModelAdmin):
    search_fields =('baslik','icerik')
    list_display = (
        'baslik','olusturulma_tarihi','duzenlenme_tarihi'
    )



@admin.register(YorumModel)
class YorumAdmin(admin.ModelAdmin):
    search_fields=('yazan_username',)

    list_display = (
        'yazan','olusturulma_tarihi','duzenlenme_tarihi'
    )


@admin.register(IletisimModel)
class IletisimAdmin(admin.ModelAdmin):
    list_display = (
        'email','olusturulma_tarihi'
    )
    search_fields =('email',)

