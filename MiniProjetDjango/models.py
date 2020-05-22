from django.db import models
from django.utils import timezone


class Fournisseur(models.Model):
    nom = models.TextField(max_length=50)
    email = models.TextField(max_length=50)
    adresse = models.TextField(max_length=50)
    telephone = models.TextField(max_length=50)
    class Meta:
        verbose_name = "fournisseur"
        ordering = ['nom']
    def __str__(self):
        return self.nom + " " + self.email+ " " + self.adresse+ " " + self.telephone

class Medicament(models.Model):
    libelle = models.TextField(max_length=50)
    categorie = models.TextField(max_length=50)
    prix = models.FloatField
    quantite = models.IntegerField
    date = models.TextField(max_length=50)
    fournisseur = models.ForeignKey('fournisseur', on_delete=models.CASCADE)
    class Meta:
        verbose_name = "medicament"
        ordering = ['date']
    def __str__(self):
        return self.libelle + " " + self.prix+ " " + self.quantite+ " " + self.date

