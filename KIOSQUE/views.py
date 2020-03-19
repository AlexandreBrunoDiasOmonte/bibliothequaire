from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Auteur, Editeur, Genre, Livre, Reservation, Utilisateur


def kiosque(request):
    livres = Livre.objects.filter(available=True).order_by('titre')
    paginator = Paginator(livres, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'KIOSQUE/kiosque.html', context)


def details(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    context = {'livre': livre}
    return render(request, 'KIOSQUE/details.html', context)


def recherche(request):
    query = request.GET.get('query')
    if not query:
        livres = Livre.objects.all().order_by('titre')
    else:
        # title contains the query is and query is not sensitive to case.
        livres = Livre.objects.filter(name__icontains=query).order_by('titre')
    if not livres.exists():
        restos = Livre.objects.filter(ville__icontains=query).order_by('titre')
    if not restos.exists():
        restos = Livre.objects.filter(codePostal__icontains=query).order_by('titre')
    results = "Résultats pour la requête < %s >" % query

    paginator = Paginator(restos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'results': results
    }
    return render(request, 'KIOSQUE/recherche.html', context)
