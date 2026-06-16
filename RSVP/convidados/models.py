from django.db import models
import os

def foto_upload_path(instance, filename):
    ext =  os.path.splitext(filename)[1]
    new_name = f"{instance.cpf}{ext}"
    return os.path.join('img/perfis/', new_name)

# Create your models here.
class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Convidados(models.Model):
    foto = models.ImageField(upload_to=foto_upload_path)
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    UF = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    eventos = models.ManyToManyField(Eventos)

    def __str__(self):
        return self.nome