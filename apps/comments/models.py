from django.db import models

from apps.kusers.models import Kuser
from apps.books.models import Book

class Comment(models.Model):
	user = models.ForeignKey(Kuser)
	title = models.CharField(max_length = 50, default="Titulo")
	body = models.TextField(default="Cuerpo del mensaje.")
	date = models.DateTimeField(auto_now_add=True)
	book = models.ForeignKey(Book)

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date']
		verbose_name=u'Comentario'
