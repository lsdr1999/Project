from django.db import models
from django.conf import settings

# Create your models here.

class Vragen(models.Model):
    id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.id}. {self.name}"

class Antwoorden(models.Model):
    id = models.ForeignKey(Vragen, on_delete=models.CASCADE, primary_key=True)
    vraag = models.CharField(max_length=240)
    eens = models.CharField(max_length=4, default="Eens")
    oneens = models.CharField(max_length=6, default="Oneens")
    geenvanbeide = models.CharField(max_length=14, default="Geen van Beide")

    def __str__(self):
        return f"{self.id}"

class Stad(models.Model):
    name = models.CharField(max_length=50)
    # ver = models.ManyToManyField(Verenigingen)
    # vivi = models.ForeignKey(Verenigingen, on_delete=models.CASCADE, related_name='Verenigingen', null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Verenigingen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=True, blank=True)
    afbeelding = models.ImageField(null=True, blank=True)
    adres = models.CharField(max_length=64, null=True, blank=True)
    leden = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    jaar = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    contributie = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    borrel = models.CharField(max_length=64, null=True, blank=True)
    ontgroening = models.CharField(max_length=64, null=True, blank=True)
    mail = models.EmailField(max_length=64, null=True, blank=True)
    website = models.URLField(max_length=64, null=True, blank=True)
    verhaal = models.CharField(max_length=600, null=True, blank=True)
    stad = models.ForeignKey(Stad, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
