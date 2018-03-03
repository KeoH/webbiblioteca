from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView

from .models import Book, Theme


class BookListView(ListView):
    model = Book
    context_object_name = 'libros'
    template_name = "lista_libros.html"


class UserPublicProfileView(DetailView):
    model = Book
    template_name = "detalle_libro.html"
    context_object_name = 'libro'


class SearchBookView(View):

    template_name = 'lista_libros.html'

    def post(self, request, *args, **kwargs):
        datos = Book.objects.all()[:2]
        ctx = {'libros': datos}
        return render(request, self.template_name, ctx)

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/')
