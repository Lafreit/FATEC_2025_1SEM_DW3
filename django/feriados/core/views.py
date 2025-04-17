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


def listar_feriados(request):
    feriados = FeriadoModel.objects.all().order_by('mes', 'dia')
    return render(request, 'listar_feriados.html', {'feriados': feriados})


from django.http import HttpResponseBadRequest
from django.shortcuts import redirect

def adicionar_feriado(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        dia = request.POST.get('dia')
        mes = request.POST.get('mes')

        # Validação simples
        if not nome or not dia or not mes:
            return HttpResponseBadRequest("Todos os campos são obrigatórios.")

        try:
            dia = int(dia)
            mes = int(mes)
            if not (1 <= dia <= 31 and 1 <= mes <= 12):
                raise ValueError
        except ValueError:
            return HttpResponseBadRequest("Dia e mês devem ser números válidos.")

        FeriadoModel.objects.create(nome=nome, dia=dia, mes=mes)
        return redirect('listar_feriados')

    return render(request, 'adicionar_feriado.html')