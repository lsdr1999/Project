from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
from django.core import serializers

from .models import *

superuser = User.objects.filter(is_superuser=True)
"""
    Initializes a superuser, which is able to log in at ./admin.
"""
if superuser.count() == 0:
    superuser = User.objects.create_user("Lars", "lars@gmail.com", "1234")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()


def index(request):
    """
        Initializes the homepage.
    """
    context = {
        "stad": Stad.objects.all(),
    }
    return render(request, "index.html", context)


def uitslag(request):
    """
        Initializes the comparison for 'kieswijzer'.

        Returns:
            A JsonResponse, which is used to compare the results
    """
    result = {}
    stadnaam = request.POST["stad"]

    for vraag in Vragen.objects.all():
        temp_dict = {}
        steden = Stad.objects.get(name__exact=stadnaam)
        for antwoord in Verant.objects.filter(vraag=vraag, stad=steden):
            temp_dict[antwoord.vereniging.name] = antwoord.antwoord
        result[vraag.id] = temp_dict

    return JsonResponse(result, content_type="application/json")


def kieswijzer(request, name):
    """
        Initializes the 'kieswijzer' page.

        Args:
            name = the name of the city selected by a user
    """
    stad = Stad.objects.get(name=name)
    verenigingen = stad.verenigingen.all()
    context = {
        "verenigingen": verenigingen,
        "verant": Verant.objects.all(),
        "vragen": Vragen.objects.all(),
        "antwoorden": Antwoorden.objects.all(),
        "test": stad,
        "stad": Stad.objects.all(),
    }
    return render(request, "kieswijzer.html", context)


def verenigingen(request, name):
    """
        Initializes the 'verenigingen' page.

        Args:
            name = the name of the city selected by a user
    """
    stad = Stad.objects.get(name=name)
    verenigingen = stad.verenigingen.all().order_by('name')
    context = {
        "verenigingen": verenigingen,
        "test": stad,
        "stad": Stad.objects.all(),
    }
    return render(request, "verenigingen.html", context)


def vereniging(request, url):
    """
        Initializes the 'vereniging' page.

        Args:
            url = the name of the 'vereniging' selected by a user
    """
    vereniging = Verenigingen.objects.get(url=url)
    context = {
        "vereniging": vereniging,
        "verenigingen": Verenigingen.objects.all(),
        "stad": Stad.objects.all(),
    }
    return render(request, "vereniging.html", context)


def woorden(request):
    """
        Initializes the 'woordenboek' page.
    """
    context = {
        "woorden": Woorden.objects.all().order_by('letter'),
        "stad": Stad.objects.all(),
    }
    return render(request, "woorden.html", context)


def test(request):
    """
        Initializes the homepage.
    """
    context = {
        "stad": Stad.objects.all(),
    }
    return render(request, "test.html", context)


def contact(request):
    """
        Initializes the contact page.
    """
    context = {
        "stad": Stad.objects.all(),
    }
    return render(request, "contact.html", context)
