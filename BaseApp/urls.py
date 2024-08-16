from django.urls import path
from . import views

urlpatterns = [
  path('', views.inicio, name='Inicio'),
  path('guitarras/', views.guitarras, name='Guitarras'),
  path('guitarras/form/', views.guitarForm, name='GuitarForm'),
  path('guitarras/search/', views.guitarSearch, name='GuitarSearch'),
  path('bajos/', views.bajos, name='Bajos'),
  path('bajos/form/', views.bassForm, name='BassForm'),
  path('bajos/search/', views.bassSearch, name='BassSearch'),
  path('clientes/', views.clientes, name='Clientes'),
  path('clientes/form/', views.clientForm, name='ClientForm'),
  path('clientes/search/', views.clientSearch, name='ClientSearch'),
  path('search-results/', views.searchResults, name='SearchResults'),
]