from django.db import models

class MotDePasse(models.Model):
    nom = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)
    # Vous pouvez ajouter d'autres champs selon vos besoins
