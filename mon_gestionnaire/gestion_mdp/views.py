from django.shortcuts import render
from .models import MotDePasse
from django.http import HttpResponse

def liste_mdp(request):
    mots_de_passe = MotDePasse.objects.all()
    return render(request, 'gestion_mdp/liste_mdp.html', {'mots_de_passe': mots_de_passe})

def accueil(request):
    return HttpResponse("Bienvenue sur le gestionnaire de mots de passe!")
