from .models import Book, Theme
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

@login_required(login_url=reverse('users:login'))
def listalibros(request):
	datos = Book.objects.all()[0:10]

	ctx = {'libros':datos}

	return render(request, 'books/lista_libros.html',ctx)

@login_required(login_url=reverse('users:login'))
def listatemas(request):
	
	temas = Theme.objects.all()

	ctx = {'temas':temas}

	return render(request, 'books/lista_temas.html',ctx)
	
@login_required(login_url=reverse('users:login'))	
def detalle_libro(request, id_libro):
	dato = Book.objects.get(pk=id_libro)
	nombreautor = dato.authors.all()
	temas = dato.theme.all()

	ctx = {'libro':dato, 'autores':nombreautor, 'temas':temas}

	return render(request, 'books/detalle_libro.html', ctx)
	
@login_required(login_url=reverse('users:login'))	
def search(request):
	if request.method == "POST":
		# Aqui el codigo que procesa la busqueda

		
		
		datos = Book.objects.all()[:2]
		ctx = { 'libros': datos }

		return render(request, 'books/lista_libros.html',ctx)
	else:
		return HttpResponseRedirect(reverse('books:home'))
