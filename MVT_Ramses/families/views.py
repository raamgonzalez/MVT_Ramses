from django.shortcuts import render
from families.models import appfamily

# Create your views here.
def family(request):
    family_01 = appfamily.objects.create(
        name = "Ross Geller",
        birth_date = "18-10-1967",
        description = "Hermano de Monica Geller, novio de Rachel Green")
    family_02 = appfamily.objects.create(
        name= "Monica Geller",
        birth_date = "22-04-1969",
        description = "Hermana de Ross Geller, novia de Chandler Bing. Obsesionada por la limpieza")
    family_03 = appfamily.objects.create(
        name= "Jack Geller",
        birth_date = "04-08-1936",
        description = "Padre de ambos y marido de Judy")
    context = {"family_01":family_01,"family_02":family_02,"family_03":family_03}
    return render(request, "family.html",context=context)