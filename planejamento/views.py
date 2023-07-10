from django.shortcuts import render
from perfil.models import *
from extrato.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from perfil.utils import calcula_total
import json


def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request, id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'Sucesso'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    despesa_mensal = calcula_total(categorias, 'valor_planejamento')
    despesa_total = sum(categoria.total_gasto() for categoria in categorias)
    percentual_mensal = int((despesa_total * 100) / despesa_mensal)
    return render(request, 'ver_planejamento.html', {'categorias': categorias, 'despesa_mensal': despesa_mensal, 'despesa_total': despesa_total, 'percentual_mensal': percentual_mensal})
