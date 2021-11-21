from django.shortcuts import redirect, render, get_object_or_404
from blog.models import Yazilar, yorum
from blog.forms import YorumEkleModelForm, yorum_ekle
from django.views import View
from django.contrib import messages


class DetayView(View):
    http_method = 'GET', 'POST'
    yorum_ekleme_formu = YorumEkleModelForm

    def get(self, request, slug):
        yazi = get_object_or_404(Yazilar, slug=slug)
        yorumlar = yazi.yorumlar.all()
        return render(request, 'pages/detay.html', context={
            'yazi': yazi,
            'yorumlar': yorumlar,
            'yorum_ekleme_formu': self.yorum_ekleme_formu,
        })

    def post(self, request, slug):
        yazi = get_object_or_404(Yazilar, slug=slug)
        yorum_ekle_form = self.yorum_ekleme_formu(request.POST)
        if yorum_ekle_form.is_valid():
            yorum = yorum_ekle_form.save(commit=False)
            yorum.yazan = request.user
            yorum.yazi = yazi
            yorum.save()
            messages.success(request, 'Succesfully is comment')
        return redirect('detay', slug=slug)
