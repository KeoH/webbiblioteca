from django.contrib import admin
from libreria.models import Editorial, Nacion, Autor, Libro, Comentario, Tema

admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Tema)
admin.site.register(Nacion)
admin.site.register(Comentario)
