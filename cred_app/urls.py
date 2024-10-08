from django.urls import path
from . import views

urlpatterns = [
    path('titulares/', views.listar_titulares, name='listar_titulares'),
]
