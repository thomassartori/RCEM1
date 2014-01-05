from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    profession =  models.CharField(max_length=200)
    lieu = models.CharField(max_length=50)
    email = models.CharField(max_length=100)


class Message(models.Model):
    auteur = models.ForeignKey(Utilisateur)
    texte = models.CharField(max_length=500)
    date = models.DateTimeField('date published')

class Filtre(models.Model):
	lieu = models.CharField(max_length=200)
	profession = models.CharField(max_length=200)    
