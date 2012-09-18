from libreria.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def home(request):
	return render_to_response('index.html')

def listalibros(request):
	datos = Libro.objects.all()
	return render_to_response('lista_libros.html',{'libro_datos':datos})
	
def listaautores(request):
	datos = Autor.objects.all()
	return render_to_response('lista_autores.html',{'autor_datos':datos})

def detalle_autor(request, id_autor):
	dato = get_object_or_404(Autor, pk=id_autor)
	return render_to_response('detalle_autor.html',{'autor':dato},context_instance=RequestContext(request))
	
def detalle_libro(request, id_libro):
	dato = get_object_or_404(Libro, pk=id_libro)
	return render_to_response('detalle_libro.html',{'libro':dato},context_instance=RequestContext(request))
	
