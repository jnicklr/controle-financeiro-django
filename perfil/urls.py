from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('gerenciar/', gerenciar, name='gerenciar'),
    path('cadastrar_banco/', cadastrar_banco, name="cadastrar_banco"),
    path('deletar_banco/<int:id>', deletar_banco, name="deletar_banco"),
    path('cadastrar_categoria/', cadastrar_categoria, name="cadastrar_categoria"),
    path('update_categoria/<int:id>', update_categoria, name="update_categoria"),
    path('dashboard/', dashboard, name="dashboard"),
]