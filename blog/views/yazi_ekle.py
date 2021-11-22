from django.views.generic import CreateView
from blog.models import Yazilar
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class YaziEkleCreateView(CreateView, LoginRequiredMixin):
    login_url = reverse_lazy('giris')
    template_name = 'pages/yazi-ekle.html'
    model = Yazilar
    fields = ['baslik', 'icerik', 'resim', 'kategoriler']

    def get_success_url(self):
        return reverse('detay', kwargs={'slug': self.objects.slug})

    def form_valid(self, form):
        yazi = form.save(commit=False)
        yazi.yazar = self.request.user
        yazi.save()
        form.save_m2m()
        return super().form_valid(form)
