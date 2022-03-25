from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse("Hello, world. You're at the Hospital General index.")

def doctor(request):
    return render(request, "HospítalGeneral/Doctor.html")

def paciente(request):
    return render(request, "HospítalGeneral/Paciente.html")

    