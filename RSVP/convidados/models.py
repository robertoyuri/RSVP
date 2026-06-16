from django.db import models

# Create your models here.
class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome