from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Vragen, Antwoorden, Stad, Verenigingen

superuser = User.objects.filter(is_superuser = True)
if superuser.count() == 0:
    superuser = User.objects.create_user("Lars", "lars@gmail.com", "1234")
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.save()

def index(request):
    return render(request, "index.html")

def kieswijzer(request):
    context = {
        "vragens": Vragen.objects.all(),
    }
    return render(request, "kieswijzer.html", context)

def verenigingen(request):
    context = {
    "verenigingen": Verenigingen.objects.all(),
    "stad": Stad.objects.all(),
    }
    return render(request, "verenigingen.html", context)

def vereniging(request):
    context = {
    "stad": Stad.objects.all(),
    "verenigingen": Verenigingen.objects.all(),
    }
    return render(request, "vereniging.html", context)

def contact(request):
    return render(request, "contact.html")
