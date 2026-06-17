from django import forms
from .models import Convidados, Eventos


class ConvidadosForm(forms.ModelForm):
    class Meta:
        model = Convidados
        fields = '__all__'
        widgets = {
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome Completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Somente números'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com.br'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(99) 99999-9999'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, Avenida, Travessa'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Casa, Apartamento'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'UF': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'00000-000'}),
            'evento': forms.SelectMultiple(attrs={'class': 'form-select', 'size':'5'}),
        }
        labels = {
            'foto': 'Foto',
            'nome': 'Nome Completo',
            'cpf': 'CPF',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'endereco': 'Endereço',
            'complemento': 'Complemento',
            'cidade': 'Cidade',
            'UF': 'UF',
            'cep': 'CEP',
            'evento': 'Evento',
        }

class EventosForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Evento'}),
            'data': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data do Evento'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Hora do Evento'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Local do Evento'}),
        }