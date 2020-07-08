from django.shortcuts import render


def accueil(request):
    return render(request, 'bibliothequaire/accueil.html')
