from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request):

    return render(request, "ProyectoWebAppVelezBeatriz/home.html")


def tienda(request):

    return render(request, "ProyectoWebAppVelezBeatriz/tienda.html")


def contacto(request):

    return render(request, "ProyectoWebAppVelezBeatriz/contacto.html")
