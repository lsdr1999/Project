from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
# from .models import Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner_platter, Order_counter, Category, User_order, Order2

def index(request):
    return render(request, "index.html")
