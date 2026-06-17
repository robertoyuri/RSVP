from django.urls import path
from .views import (home, convidadoslistar, convidadoscadastrar, eventolistar,eventocadastrar,
                    convidadoseditar, convidadosexcluir, eventoeditar, eventoexcluir)

app_name = 'convidados'

urlpatterns = [
    path('', home, name='home'),
    path('convidadoscadastrar/', convidadoscadastrar, name='convidadoscadastrar'),
    path('convidadoslistar/', convidadoslistar, name='convidadoslistar'),
    path('convidadoseditar/<int:id>/', convidadoseditar, name='convidadoseditar'),
    path('convidadosexcluir/<int:id>/', convidadosexcluir, name='convidadosexcluir'),
    path('eventocadastrar/', eventocadastrar, name='eventocadastrar'),
    path('eventolistar/', eventolistar, name='eventolistar'),
    path('eventoeditar/<int:id>/', eventoeditar, name='eventoeditar'),
    path('eventoexcluir/<int:id>/', eventoexcluir, name='eventoexcluir'),
]