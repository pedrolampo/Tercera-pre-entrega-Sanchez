from django.http import HttpResponse
from django.shortcuts import render
from .models import Guitar, Bass, Client

# Create your views here.
def inicio(req):
  return render(req, 'BaseApp/index.html')

def guitarras(req):
  return render(req, 'BaseApp/guitarras.html')

def bajos(req):
  return render(req, 'BaseApp/bajos.html')

def clientes(req):
  return render(req, 'BaseApp/clientes.html')




def guitarForm(req):
  if req.method == "POST":
    guitarra = Guitar(name=req.POST['guitar'], price=req.POST['price'])
    guitarra.save()
    return render(req, 'BaseApp/index.html')

  return render(req, 'BaseApp/guitar-form.html')

def bassForm(req):
  if req.method == "POST":
    bajo = Bass(name=req.POST['bass'], price=req.POST['price'])
    bajo.save()
    return render(req, 'BaseApp/index.html')

  return render(req, 'BaseApp/bass-form.html')

def clientForm(req):
  if req.method == "POST":
    client = Client(name=req.POST['name'], surname=req.POST['surname'], email=req.POST['email'])
    client.save()
    return render(req, 'BaseApp/index.html')

  return render(req, 'BaseApp/client-form.html')




def guitarSearch(req):
  return render(req, 'BaseApp/search-guitar.html')

def bassSearch(req):
  return render(req, 'BaseApp/search-bass.html')

def clientSearch(req):
  return render(req, 'BaseApp/search-client.html')




def searchResults(req):
  guitar_query = req.GET.get('guitar')
  bass_query = req.GET.get('bass')
  client_query = req.GET.get('client')
  
  if guitar_query:
    nombre = guitar_query
    guitarras = Guitar.objects.filter(name__icontains=nombre)
    print(guitarras)
    return render(req, "BaseApp/results.html", { "name": nombre, "guitars": guitarras })

  elif bass_query:
    nombre = bass_query
    bajos = Bass.objects.filter(name__icontains=nombre)
    return render(req, "BaseApp/results.html", { "name": nombre, "basses": bajos })

  elif client_query:
    nombre = client_query
    clientes = Client.objects.filter(name__icontains=nombre)
    return render(req, "BaseApp/results.html", { "name": nombre, "clients": clientes })

  else:
    respuesta = "No enviaste nada"

  return HttpResponse(respuesta)