from django import forms
from blog.models import Yazilar


class YaziGuncelleFormModel(forms.ModelForm):
    class Meta:
        model = Yazilar
        exclude = ('yazar','slug')
        
        