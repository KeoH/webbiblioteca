from django.shortcuts import render

from .models import Book, Theme

def listalibros(request):
	datos = Book.objects.all()

	ctx = {'libros':datos}

	return render(request, 'books/lista_libros.html',ctx)

def listatemas(request):
	
	temas = Theme.objects.all()

	ctx = {'temas':temas}

	return render(request, 'books/lista_temas.html',ctx)
	
def detalle_libro(request, id_libro):
	dato = Book.objects.get(pk=id_libro)
	nombreautor = dato.authors.all()
	temas = dato.theme.all()

	ctx = {'libro':dato, 'autores':nombreautor, 'temas':temas}

	return render(request, 'books/detalle_libro.html', ctx)
	