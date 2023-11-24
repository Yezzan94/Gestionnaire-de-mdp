from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    # autres motifs d'URL...
]
