from libreria.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def home(request):
	return render_to_response('index.html')

def listalibros(request):
	datos = Libro.objects.all()
	return render_to_response('lista_libros.html',{'libros':datos})
	
def listaautores(request):
	datos = Autor.objects.all()
	return render_to_response('lista_autores.html',{'autores':datos})

def detalle_autor(request, id_autor):
	dato = get_object_or_404(Autor, pk=id_autor)
	datonacion = Nacion.objects.filter(nacion_nombre = dato.autor_nacion)
	bandera = datonacion[0].nacion_bandera
	datolibro = Libro.objects.filter(libro_autores=id_autor)
	numlibros = datolibro.count()
	return render_to_response('detalle_autor.html',{'autor':dato, 'libros':datolibro, 'numlibros':numlibros, 'nacion':datonacion, 'urlbandera':bandera},context_instance=RequestContext(request))
	
def detalle_libro(request, id_libro):
	dato = get_object_or_404(Libro, pk=id_libro)
	nombreautor = Libro.objects.filter(id=id_libro)
	nombres = nombreautor[0].libro_autores.all()
	temas = nombreautor[0].libro_tema.all()

	return render_to_response('detalle_libro.html',{'libro':dato, 'autores':nombres, 'temas':temas},context_instance=RequestContext(request))
	
