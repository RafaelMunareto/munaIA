
from django.shortcuts import render

def listar(request):
    """ CARREGA A TABELA PRINCIPAL COM OS DADOS """
    dados = {
        'title': 'HOME',
    }
    return render(request, 'home/index.html', dados)