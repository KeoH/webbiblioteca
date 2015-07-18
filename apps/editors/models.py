from django.db import models

class Editor(models.Model):
	name = models.CharField(max_length = 255)
	website = models.URLField(blank=True)
	logo = models.ImageField(upload_to="editorLogo/", blank=True)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		ordering = ['name']
		verbose_name=u'Editorial'
		verbose_name_plural=u'Editoriales'