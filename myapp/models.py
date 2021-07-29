from django.conf import settings

from django.db import models
from django.db.models.fields import IntegerField

class Article(models.Model):
    name=models.CharField(max_length=20)
    myuser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    class Meta:
        db_table='articles'
    def __str__(self):
        return self.name
class Mouvement(models.Model):
    nom=models.CharField(max_length=20)
    qte = models.CharField(max_length=10)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    class Meta:
        db_table='mouvements'


class Grade(models.Model):
    libelle=models.CharField(max_length=40)
    position=IntegerField()
    class Meta:
        db_table='grades'
    def __str__(self):
        return self.libelle

class Personne(models.Model):
    nom=models.CharField(max_length=20)
    prenom=models.CharField(max_length=20)
    date_created=models.DateField(auto_now_add=True,null=True)
    date_entr=models.DateField(auto_now_add=False,auto_now=False,null=True)
    year_prod=models.IntegerField(null=True)
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE,null=True)
    
    class Meta:
        db_table='personnes'
        ordering = ['id']

# Create your models here.
