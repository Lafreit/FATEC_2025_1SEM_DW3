from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel
from core.service import teste

def feriado(requests):
    hoje = datetime.today()
    qs = FeriadoModel.objects.filter(mes=hoje.month)
    qs = qs.filter(dia=hoje.day)
    # Comentado para evitar erros em uma máquina sem MongoDB
    # teste()
    if len(qs) > 0:
        contexto = {'feriado': True, 'nome':qs[0].nome}
    else:
        contexto = {'feriado': False}
    return render(requests, "feriado.html", contexto)