from .models import Author, Nation
from books.models import Book
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render

@login_required(login_url=reverse('users:login'))
def listaautores(request):
	datos = Author.objects.all()[0:5]
	return render(request, 'authors/lista_autores.html',{'autores':datos})

@login_required(login_url=reverse('users:login'))
def detalle_autor(request, id_autor):
	dato = Author.objects.get(pk=id_autor)
	datonacion = dato.nation
	bandera = datonacion.flag
	datolibro = Book.objects.filter(authors=id_autor)
	numlibros = datolibro.count()

	ctx = {	'autor':dato,
			'libros':datolibro,
			'numlibros':numlibros,
			'nacion':datonacion,
			'urlbandera':bandera
			}

	return render(request, 'authors/detalle_autor.html',ctx)
	
