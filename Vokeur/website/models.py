from django.db import models
from django.conf import settings

# Create your models here.

class Vragen(models.Model):
    id = models.DecimalField(max_digits=4, decimal_places=0, primary_key=True)
    name = models.CharField(max_length=240)

    def __str__(self):
        return f"{self.id} - {self.name}"

class Antwoorden(models.Model):
    EENS = 'Eens'
    ONEENS = 'Oneens'
    GEENVANBEIDE = 'Geen van beide'
    ANTWOORDEN = [
        (EENS, 'Eens'),
        (ONEENS, 'Oneens'),
        (GEENVANBEIDE, 'Geen van beide'),
    ]
    antwoorden = models.CharField(
        max_length=15,
        choices=ANTWOORDEN,
        default=None,
    )

    def is_upperclass(self):
        return self.antwoorden in (self.EENS, self.ONEENS, self.GEENVANBEIDE)

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
