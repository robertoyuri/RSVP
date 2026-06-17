from django.shortcuts import render, redirect
from .forms import ConvidadosForm

from .models import Eventos, Convidados

def home(request):
    pais = 'Gana'
    return render(request, 'home.html', {'pais':pais})

def convidadoscadastrar(request):
    form = ConvidadosForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('convidados:convidadoslistar')
        else:
            form = ConvidadosForm()
    return render(request, 'convidados/convidadoscadastrar.html', {'form':form})

def convidadoslistar(request):
    convidados = Convidados.objects.all()
    return render(request, 'convidados/convidadoslistar.html',{'convidados':convidados})

def eventocadastrar(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        data = request.POST['data']
        hora = request.POST['hora']
        local = request.POST['local']
        evento = Eventos(nome=nome, data=data, hora=hora, local=local).save()
        return redirect('convidados:convidadoslistar')
    return render(request, 'convidados/eventocadastrar.html')

def eventolistar(request):
    eventos = Eventos.objects.all()
    return render(request, 'convidados/eventolistar.html',{'eventos':eventos})