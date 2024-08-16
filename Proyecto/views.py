# from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader

# Create your views here.
def inicio(req):
  return HttpResponse("<h1>Proyecto Python Pedro Sanchez</h1><a href=\"BaseApp\"><button>Ir a la App</button></a>")