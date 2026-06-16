from cgi import print_form

from django.shortcuts import render, redirect
from six import print_

from .models import Eventos

def home(request):
    pais = 'Gana'
    return render(request, 'home.html', {'pais':pais})

def cadastro(request):
    return render(request, 'convidados/cadastro.html')

def listar(request):
    return render(request, 'convidados/listar.html',{'convidados':range(50)})

def eventocadastrar(request):
    print('Eventos cadastradas')
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        nome = request.POST['nome']
        data = request.POST['data']
        hora = request.POST['hora']
        local = request.POST['local']
        evento = Eventos(nome=nome, data=data, hora=hora, local=local).save()
        print(evento)
        return redirect('convidados:eventolistar')
    return render(request, 'convidados/eventocadastrar.html')

def eventolistar(request):
    eventos = Eventos.objects.all()
    return render(request, 'convidados/eventolistar.html',{'eventos':eventos})