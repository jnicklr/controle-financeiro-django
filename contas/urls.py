from django.urls import path
from .views import *

urlpatterns = [
    path('definir_contas/', definir_contas, name="definir_contas"),
    path('ver_contas/', ver_contas, name="ver_contas"),
]