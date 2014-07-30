from django.db import models

from authors.models import Author
from editors.models import Editor


class Theme(models.Model):
	name = models.CharField(max_length = 30)

	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name=u'Tema'

class Book(models.Model):

	registro = models.CharField(max_length = 10, default="0000-A")
	title = models.CharField(max_length = 255)
	authors = models.ManyToManyField(Author)
	editor = models.ForeignKey(Editor)
	theme = models.ManyToManyField(Theme)
	pub_year = models.CharField(max_length=4, default="2014")
	resume = models.TextField(default="Resumen...")
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		ordering = ['title']
		verbose_name=u'Libro'