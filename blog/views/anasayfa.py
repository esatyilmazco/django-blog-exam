from django.shortcuts import render



def anasayfa(request):
    context ={
        'isim': 'Esat'
    }
    return render(request,'pages/anasayfa.html',context=context)

