from django.urls import path
from .views import home, cadastro, listar, eventolistar, eventocadastrar

app_name = 'convidados'

urlpatterns = [
    path('', home, name='home'),
    path('/cadastro/', cadastro, name='cadastro'),
    path('/listar/', listar, name='listar'),
    path('/eventocadastrar/', eventocadastrar, name='eventocadastrar'),
    path('eventolistar/', eventolistar, name='eventolistar'),
]