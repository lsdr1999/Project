from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Vragen, Antwoorden, Stad, Verenigingen, Letter, Woorden

superuser = User.objects.filter(is_superuser = True)
if superuser.count() == 0:
    superuser = User.objects.create_user("Lars", "lars@gmail.com", "1234")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()

def index(request):
    context = {
        "stad": Stad.objects.all(),
    }
    return render(request, "index.html", context)

def kieswijzer(request):
    context = {
        "vragen": Vragen.objects.all(),
        "antwoorden": Antwoorden.objects.all(),
        "stad": Stad.objects.all(),
    }
    return render(request, "kieswijzer.html", context)

def verenigingen(request, name):
    stad = Stad.objects.get(name=name)
    verenigingen = stad.verenigingen.all()
    context = {
        "verenigingen": verenigingen,
        "test": stad,
        "stad": Stad.objects.all(),
    }
    return render(request, "verenigingen.html", context)

def vereniging(request, url):
    vereniging = Verenigingen.objects.get(url=url)
    context = {
        "vereniging": vereniging,
        "verenigingen": Verenigingen.objects.all(),
        "stad": Stad.objects.all(),
    }
    return render(request, "vereniging.html", context)

def woorden(request):
    context = {
        "woorden": Woorden.objects.all(),
        "stad": Stad.objects.all(),
    }
    return render(request, "woorden.html", context)

def contact(request):
    context = {
        "stad": Stad.objects.all(),
    }
    return render(request, "contact.html", context)
