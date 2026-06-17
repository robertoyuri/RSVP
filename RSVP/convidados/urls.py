from django.urls import path
from .views import home, convidadoslistar, convidadoscadastrar, eventolistar, eventocadastrar

app_name = 'convidados'

urlpatterns = [
    path('', home, name='home'),
    path('convidadoscadastrar/', convidadoscadastrar, name='convidadoscadastrar'),
    path('convidadoslistar/', convidadoslistar, name='convidadoslistar'),
    path('eventocadastrar/', eventocadastrar, name='eventocadastrar'),
    path('eventolistar/', eventolistar, name='eventolistar'),
]