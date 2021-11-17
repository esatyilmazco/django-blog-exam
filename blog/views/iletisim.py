from django.shortcuts import render

def iletisim(request):
    context = {
        'sayi':5
    }
    return render(request,'pages/iletisim.html',context=context)



