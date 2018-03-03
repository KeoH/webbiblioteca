from django.db import models

class Editor(models.Model):
	name = models.CharField(max_length = 255)
	website = models.URLField(blank=True)
	logo = models.ImageField(upload_to="editorLogo/", blank=True)
	
	def __str__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name='Editorial'
		verbose_name_plural='Editoriales'