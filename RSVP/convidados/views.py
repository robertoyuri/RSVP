from django.shortcuts import render, redirect, get_object_or_404
from .forms import ConvidadosForm, EventosForm

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

def convidadoseditar(request, id):
    convidado = None
    if id:
        convidado = get_object_or_404(Convidados, pk=id)

    if request.method == 'POST':
        form = ConvidadosForm(request.POST, request.FILES, instance=convidado)

        if form.is_valid():
            form.save()
            return redirect('convidados:convidadoslistar')
    else:
        form = ConvidadosForm(instance=convidado)
    return render(request, 'convidados/convidadoscadastrar.html', {'form':form})

def convidadosexcluir(request, id):
    convidado = get_object_or_404(Convidados, pk=id)
    if request.method == 'POST':
        convidado.delete()
    return redirect('convidados:convidadoslistar')

def eventocadastrar(request):
    form = EventosForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('convidados:eventolistar')
        else:
            form = EventosForm()
    return render(request, 'convidados/eventocadastrar.html', {'form':form})

def eventolistar(request):
    eventos = Eventos.objects.all()
    return render(request, 'convidados/eventolistar.html',{'eventos':eventos})

def eventoeditar(request, id):
    evento = None
    if id:
        evento = get_object_or_404(Eventos, pk=id)

    if request.method == 'POST':
        form = EventosForm(request.POST, request.FILES, instance=evento)

        if form.is_valid():
            form.save()
            return redirect('convidados:eventolistar')
    else:
        form = EventosForm(instance=evento)
    return render(request, 'convidados/eventoCadastrar.html', {'form':form})

def eventoexcluir(request, id):
    evento = get_object_or_404(Eventos, pk=id)
    if request.method == 'POST':
        evento.delete()
    return redirect('convidados:eventolistar')