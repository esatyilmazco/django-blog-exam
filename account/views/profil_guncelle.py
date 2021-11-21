from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.forms import ProfilDuzenlemeForm
from django.contrib import messages


@login_required(login_url='/')
def profil_guncelle(request):
    if request.method == 'POST':
        form = ProfilDuzenlemeForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile is edit')
    else:
        form = ProfilDuzenlemeForm(instance=request.user)
    return render(request, 'pages/profil-guncelle.html', context={
        'form': form,
    })
