from django.urls import path
from .views import *
from perfil.models import *
from extrato.models import *

urlpatterns = [
    path('definir_planejamento/', definir_planejamento, name="definir_planejamento"),
    path('update_valor_categoria/<int:id>', update_valor_categoria, name="update_valor_categoria"),
    path('ver_planejamento/', ver_planejamento, name="ver_planejamento"),
]