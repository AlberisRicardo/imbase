from django.shortcuts import render
from imagens.forms import FormularioLogin, FormularioFotos, FormularioEditarFotos
from imagens.models import Fotos
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login as login_authenticate
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_request
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
	template = 'home.html'

	form = FormularioFotos()
	contexto = {'forms': form}

	fotos = Fotos.objects.filter(user = request.user.id).order_by('-data_postagem')

	contexto['fotos'] = fotos
	return render(request, template, contexto) 


@login_required()
def cadastrar(request):

	if(request.method == 'POST'):
		form = FormularioFotos(request.POST, request.FILES)
		if(form.is_valid()):
			titulo = form.cleaned_data['Titulo']
			imagem = form.cleaned_data['Imagem']
			fotos = Fotos(titulo = titulo, imagem = imagem, user = request.user)
			fotos.save()
			messages.success(request, "Imagem cadastrada com sucesso!")
			return HttpResponseRedirect("/imbase/home/")
	form = FormularioFotos()

	contexto = {'forms': form}

	return render(request, "cadastrar.html", contexto)


@login_required()
def excluir(request, id_imagem):

	foto = Fotos.objects.get(id=id_imagem)
	foto.delete()
	messages.success(request, "Imagem apagada com sucesso!")

	return HttpResponseRedirect("/imbase/home/")


@login_required()
def editar(request, id_imagem):

	if(request.method == 'POST'):
		foto = Fotos.objects.get(id=id_imagem)
		titulo = request.POST.get("Titulo", None)

		try:
			imagem = request.FILES["Imagem"]
		except:
			imagem = None
		if(imagem != None):
			foto.imagem = imagem
		if(titulo != None and len(titulo.strip()) > 0):
			foto.titulo = titulo
		foto.save()
		messages.success(request, "Imagem editada com sucesso!")
		return HttpResponseRedirect("/imbase/home/")

	foto = Fotos.objects.get(id=id_imagem)
	form = FormularioEditarFotos(initial={"Titulo": foto.titulo})
	contexto = {'forms': form , 'url_foto': foto.imagem.url}
	return render(request, "editar.html", contexto)

def login(request):
	if(request.method == 'POST'):
		form = FormularioLogin(request.POST)
		if(form.is_valid()):
			login = form.cleaned_data["login"]
			senha = form.cleaned_data["senha"]
			user = authenticate(username=login, password=senha)
			if(user is not None):
				login_authenticate(request, user)
				return HttpResponseRedirect("/imbase/home/")
			else:
 				messages.error(request, "Login ou senha não compativeis")
 				return HttpResponseRedirect("/imbase/")
	form = FormularioLogin()
	contexto = {'forms': form}
	return render(request, "login.html", contexto)

def logout(request):
	logout_request(request)
	return HttpResponseRedirect("/imbase/")

