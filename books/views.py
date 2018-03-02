from .models import Book, Theme
#from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.detail import DetailView
from django.views.generic import ListView, View

#from core.views import LoginRequiredMixin

class BookListView(ListView):
    model = Book
    context_object_name = 'libros'
    template_name = "lista_libros.html"


# @login_required(login_url=reverse('users:login'))
# def listalibros(request):
# 	datos = Book.objects.all()[0:10]
#
# 	ctx = {'libros':datos}
#
# 	return render(request, 'books/lista_libros.html',ctx)

# @login_required(login_url=reverse('users:login'))
# def listatemas(request):
#
# 	temas = Theme.objects.all()
#
# 	ctx = {'temas':temas}
#
# 	return render(request, 'books/lista_temas.html',ctx)
#

class UserPublicProfileView(DetailView):
    model = Book
    template_name = "detalle_libro.html"
    context_object_name = 'libro'


# @login_required(login_url=reverse('users:login'))
# def detalle_libro(request, id_libro):
# 	dato = Book.objects.get(pk=id_libro)
# 	nombreautor = dato.authors.all()
# 	temas = dato.theme.all()
#
# 	ctx = {'libro':dato, 'autores':nombreautor, 'temas':temas}
#
# 	return render(request, 'books/detalle_libro.html', ctx)
#

class SearchBookView(View):

    template_name = 'lista_libros.html'

    def post(self, request, *args, **kwargs):
        datos = Book.objects.all()[:2]
        ctx = { 'libros': datos }
        return render(request, self.template_name, ctx)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse('books:booklist'))

# @login_required(login_url=reverse('users:login'))
# def search(request):
# 	if request.method == "POST":
# 		# Aqui el codigo que procesa la busqueda
#
#
#
# 		datos = Book.objects.all()[:2]
# 		ctx = { 'libros': datos }
#
# 		return render(request, 'books/lista_libros.html',ctx)
# 	else:
# 		return HttpResponseRedirect(reverse('books:home'))
