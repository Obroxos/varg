#Permite crear, actualizar y editar modelos.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
#Permite listar modelos.
from django.views.generic.list import ListView
#Permite ver modelos en detalle.
from django.views.generic.detail import DetailView
#Permite hacer render de páginas.
from django.shortcuts import render, HttpResponse, redirect
#Importa modelos
from .models import Post, Reglamento, Clase, Condominio, Automatizacion
from django.contrib.auth import login
from django.contrib import messages

def dashboard(request):
	return render(request, 'core/admin_dashboard.html')

def perfil(request):
	return render(request, 'core/admin_perfil.html')

class LandingView(ListView):
	model = Clase
	template_name = 'core/static_landing.html'

def ley(request):
	return render(request, 'core/static_ley.html')

def asambleas(request):
	return render(request, 'core/static_asambleas.html')

def completado(request):
	return render(request, 'core/static_completado.html')

def fallido(request):
	return render(request, 'core/static_fallido.html')

def plan(request):
	return render(request, 'core/static_plan.html')
##### MODELO DE ENTRADAS DE BLOGstatic_


class PostCreate(CreateView):
	model = Post
	fields = ['title', 'subtitle', 'content', 'image', 'author']
	template_name = 'core/admin_entradas_crear.html'
	success_url ="/admin/entradas"

class PostUpdateView(UpdateView):
	model = Post
	fields = ['title', 'subtitle', 'content', 'image', 'author']
	template_name = 'core/admin_entradas_crear.html'
	success_url ="/admin/entradas"

class PostDeleteView(DeleteView):
	model = Post
	template_name = 'core/admin_entradas_eliminar.html'
	success_url ="/admin/entradas"

class PostListView(ListView):
	model = Post

class PostDetailView(DetailView):
	model = Post



class ClaseCreate(CreateView):
	model = Clase
	fields = ['title', 'subtitle', 'content', 'video', 'image', 'author']
	template_name = 'core/admin_clases_crear.html'
	success_url ="/admin/clases"

class ClaseUpdateView(UpdateView):
	model = Clase
	fields = ['title', 'subtitle', 'content', 'video',  'image', 'author']
	template_name = 'core/admin_clases_crear.html'
	success_url ="/admin/clases"

class ClaseDeleteView(DeleteView):
	model = Clase
	template_name = 'core/admin_clases_eliminar.html'
	success_url ="/admin/clases"

class ClaseListView(ListView):
	model = Clase

class ClaseDetailView(DetailView):
	model = Clase




class CondominioCreate(CreateView):
	model = Condominio
	fields = ['name', 'rut', 'direccion', 'comuna', 'region', 'admin']
	template_name = 'core/admin_condominios_crear.html'
	success_url ="/admin/condominios"

class CondominioUpdateView(UpdateView):
	model = Condominio
	fields = ['name', 'rut', 'direccion', 'comuna', 'region', 'admin']
	template_name = 'core/admin_condominios_crear.html'
	success_url ="/admin/condominios"

class CondominioDeleteView(DeleteView):
	model = Condominio
	template_name = 'core/admin_condominios _eliminar.html'
	success_url ="/admin/condominios"

class CondominioListView(ListView):
	model = Condominio

class CondominioDetailView(DetailView):
	model = Condominio






class AutomatizacionCreate(CreateView):
	model = Automatizacion
	fields = ['lanzador', 'codigo', 'descripcion', 'efecto']
	template_name = 'core/admin_automatizacion_crear.html'
	success_url ="/admin/automatizaciones"

class AutomatizacionUpdateView(UpdateView):
	model = Automatizacion
	fields = ['lanzador', 'codigo', 'descripcion', 'efecto']
	template_name = 'core/admin_automatizacion_crear.html'
	success_url ="/admin/automatizaciones"

class AutomatizacionDeleteView(DeleteView):
	model = Automatizacion
	template_name = 'core/admin_automatizacion_eliminar.html'
	success_url ="/admin/automatizaciones"

class AutomatizacionListView(ListView):
	model = Automatizacion

class AutomatizacionDetailView(DetailView):
	model = Automatizacion
