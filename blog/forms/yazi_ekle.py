from django import forms
from django.forms import fields
from blog.models import Yazilar



class YaziEkleModelForm(forms.ModelForm):
        class Meta:
            model = Yazilar
            exclude = ('yazar','slug')
            
        