from django import forms
from django.contrib.auth.models import User


class FormularioLogin(forms.Form):
	login = forms.CharField(label = 'login', max_length=50)
	senha = forms.CharField(label = 'senha', max_length = 50, widget=forms.PasswordInput())

class FormularioFotos(forms.Form):
	Imagem = forms.ImageField(label = 'Imagem')
	Titulo = forms.CharField(label = 'Titulo', max_length =50)

class FormularioEditarFotos(forms.Form):
	Imagem = forms.ImageField(label = 'Imagem', required= False)
	Titulo = forms.CharField(label = 'Titulo', max_length =50, required= False)