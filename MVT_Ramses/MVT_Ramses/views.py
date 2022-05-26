from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def bienvenido(request):
    return HttpResponse("<h2>Bienvenido a mi prueba de MVT<h2>")

