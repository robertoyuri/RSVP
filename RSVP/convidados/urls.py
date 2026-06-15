from django.urls import path
from .views import home, cadastro, listar

app_name = 'convidados'

urlpatterns = [
    path('', home, name='home'),
    path('/cadastro/', cadastro, name='cadastro'),
    path('/listar/', listar, name='listar'),
]