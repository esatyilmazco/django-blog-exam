from django import forms

class IletisimForm(forms.Form):
    email = forms.EmailField(label='E-Post',max_length=100)
    isim_soyisim = forms.CharField(label='Name and Surname',max_length=25,attrs={'class':'form-control'})
    mesaj = forms.CharField(label='Your Message',widget=forms.Textarea)