from django import forms
from datetime import datetime
from passagens.validations import *

CLASSES = [('Econômica', 'Econômica'), ('Executiva', 'Executiva'), ('Primeira Classe', 'Primeira Classe')]

class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100 , widget=forms.TextInput(attrs={'class': 'form-control'}))
    origem.label_classes = 'form-label'
    destino = forms.CharField(label='Destino', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    destino.label_classes = 'form-label'
    data_ida = forms.DateField(label='Data Ida', widget=forms.widgets.DateInput(attrs={	'type': 'date', 'class': 'form-control'}))
    data_ida.label_classes = 'form-label'
    data_volta = forms.DateField(label='Data Volta', widget=forms.widgets.DateInput(attrs={	'type': 'date', 'class': 'form-control'}))
    data_volta.label_classes = 'form-label'
    data_pesquisa = forms.DateField(label='Data da pesquisa', widget=forms.widgets.DateInput(attrs={	'type': 'date', 'class': 'form-control'}), disabled=True, initial=datetime.today)
    data_pesquisa.label_classes = 'form-label'
    tipo_classe = forms.CharField(label='Classe', widget=forms.Select(choices=CLASSES, attrs={'class': 'form-select'}))
    tipo_classe.label_classes = 'form-label'
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email.label_classes = 'form-label'
    
    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_de_erros = {}
        campo_tem_algum_numero(origem, 'origem',lista_de_erros)
        campo_tem_algum_numero(destino, 'destino',lista_de_erros)
        origem_destino_iguais(origem, destino, lista_de_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros)
        data_ida_menor_data_de_hoje(data_ida, data_pesquisa, lista_de_erros)
        if lista_de_erros is not None:
            for erro in lista_de_erros:
                mensagem_erro = lista_de_erros[erro]
                self.add_error(erro, mensagem_erro)
        return self.cleaned_data