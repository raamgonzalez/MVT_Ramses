from django.shortcuts import render
from families.models import appfamily
from django.http import HttpResponse

# Create your views here.
def family(request):
    family_01 = appfamily(
        name = "Ross Geller",
        birth_date = "18-10-1967",
        description = "Hermano de Monica Geller, novio de Rachel Green",
        )
    family_01.save()
    
    family_02 = appfamily(
        name= "Monica Geller",
        birth_date = "22-04-1969",
        description = "Hermana de Ross Geller, novia de Chandler Bing. Obsesionada por la limpieza",
        )
    family_02.save()
    
    family_03 = appfamily(
        name= "Jack Geller",
        birth_date = "04-08-1936",
        description = "Padre de ambos y marido de Judy",
        )
    family_03.save()
    
    context = appfamily.objects.all()
    return render(request, "family.html",{"context":context})

def bienvenido(request):
    return HttpResponse("<h2>Bienvenido a mi prueba de MVT<h2>")