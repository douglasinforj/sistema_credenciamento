from django.shortcuts import render
from .models import Titular


def listar_titulares(request):
    titulares = Titular.objects.all() 
    return render(request, 'cred_app/listar_titulares.html', {'titulares': titulares})
