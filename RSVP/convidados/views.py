from django.shortcuts import render

def home(request):
    pais = 'Gana'
    return render(request, 'home.html', {'pais':pais})

def cadastro(request):
    return render(request, 'convidados/cadastro.html')
