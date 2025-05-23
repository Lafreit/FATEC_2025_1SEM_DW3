from django.shortcuts import render
from datetime import datetime
from core.models import FeriadoModel
from core.service import teste
from django.http import JsonResponse

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
from core.forms import FeriadoForm, FeriadoForm2

def adicionar_feriado(request):
    if request.method == 'POST':
        form = FeriadoForm(request.POST)
        if form.is_valid():
            FeriadoModel.objects.create(**form.cleaned_data)
            return redirect('listar_feriados')
    else:
        form = FeriadoForm2()
    return render(request, 'adicionar_feriado.html', {'form':form})


from django.shortcuts import get_object_or_404

def deletar_feriado(request, feriado_id):
    feriado = get_object_or_404(FeriadoModel, id=feriado_id)
    if request.method == 'POST':
        feriado.delete()
        return redirect('listar_feriados')
    return render(request, 'confirmar_delete.html', {'feriado': feriado})


def atualizar_feriado(request, feriado_id):
    feriado = get_object_or_404(FeriadoModel, id=feriado_id)
    if request.method == 'POST':
        form = FeriadoForm2(request.POST, instance=feriado)
        if form.is_valid():
            form.save()
            return redirect('listar_feriados')
    else:
        form = FeriadoForm2(instance=feriado)
    return render(request, 'atualizar_feriado.html', {'form': form, 'feriado': feriado})


def listar_feriados_json(request):
    feriados = FeriadoModel.objects.all().values('id', 'nome', 'dia', 'mes')
    return JsonResponse(list(feriados),safe=False)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FeriadoModel
from .serializers import FeriadoSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class FeriadoListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        feriados = FeriadoModel.objects.all()
        serializer = FeriadoSerializer(feriados, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeriadoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FeriadoDetailView(APIView):
    def get(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        serializer = FeriadoSerializer(feriado)
        return Response(serializer.data)

    def put(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        serializer = FeriadoSerializer(feriado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        feriado = get_object_or_404(FeriadoModel, pk=pk)
        feriado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)