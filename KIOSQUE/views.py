from django.shortcuts import render


def kiosque(request):
    return render(request, 'KIOSQUE/kiosque.html')
