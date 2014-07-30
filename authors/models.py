#encoding:utf-8
from django.db import models

class Nation(models.Model):
	name = models.CharField(max_length = 255)
	flag = models.ImageField(upload_to="nationFlags/", blank=True)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name=u'País'
		verbose_name_plural = u'Paises'

class Author(models.Model):
	
	SEXO_CHOICES = (
	    ('H', 'Hombre'),
	    ('M', 'Mujer'),)
	
	name = models.CharField(max_length = 255)
	sex = models.CharField(max_length=1, choices=SEXO_CHOICES, default='H')
	photo = models.ImageField(upload_to="authorPhoto/", blank=True)
	nation = models.ForeignKey(Nation)

	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name=u'Autor'
		verbose_name_plural = u'Autores'