#encoding:utf-8
from django.db import models
from django.conf import settings

class Nation(models.Model):
	name = models.CharField(max_length = 255)
	flag = models.ImageField(upload_to="nationFlags/", blank=True)

	def get_flag(self):
		if(self.flag):
			return self.flag.url
		else:
			return settings.STATIC_URL+'img/no-flag.jpeg'
	
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

	def get_photo(self):
		if self.photo:
			photo_url = self.photo.url
		else:	
			photo_url = settings.STATIC_URL+'img/default.png'
		return photo_url

	def get_sexo_image(self):
		if self.sex == 'H':
			url = settings.STATIC_URL+'img/male.png'
		else:
			url = settings.STATIC_URL+'img/female.png'
		return url

	def get_sexo_name(self):
		if self.sex == 'H':
			name = 'Hombre'
		else:
			name = 'Mujer'
		return name

	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name=u'Autor'
		verbose_name_plural = u'Autores'