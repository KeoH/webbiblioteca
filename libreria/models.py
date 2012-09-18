from django.db import models

class Usuario(models.Model):
	usuario_nick = models.CharField(max_length = 10)
	usuario_nombre = models.CharField(max_length = 25)
	
	def __unicode__(self):
		return self.usuario_nick
		
	class Meta:
		ordering = ['usuario_nick']

class Editorial(models.Model):
	editorial_nombre = models.CharField(max_length = 60)
	editorial_website = models.URLField(default="www.google.es")
	editorial_logotipo = models.URLField(default="http://upload.wikimedia.org/wikipedia/commons/5/57/Logotipo_de_Canal_Trece.JPG")
	
	def __unicode__(self):
		return self.editorial_nombre
		
	class Meta:
		ordering = ['editorial_nombre']
	
class Nacion(models.Model):
	nacion_nombre = models.CharField(max_length = 30)
	nacion_bandera = models.URLField(default="http://soymino.files.wordpress.com/2010/07/bandera_espana.jpg")
	
	def __unicode__(self):
		return self.nacion_nombre
		
	class Meta:
		ordering = ['nacion_nombre']
	
class Autor(models.Model):
	
	SEXO_CHOICES = (
	    ('H', 'Hombre'),
	    ('M', 'Mujer'),)
	
	autor_nombre = models.CharField(max_length = 60)
	autor_sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='H')
	autor_foto = models.URLField(default = "http://3.bp.blogspot.com/-o20K2YGyyDs/Tdvv4FoZu2I/AAAAAAAABLo/A-gYxef90OA/s1600/mafalda-escritora.jpg")
	autor_nacion = models.ForeignKey(Nacion)

	def __unicode__(self):
		return self.autor_nombre
		
	class Meta:
		ordering = ['autor_nombre']

class Comentario(models.Model):
	comentario_usuario = models.ForeignKey(Usuario)
	comentario_titulo = models.CharField(max_length = 50)
	comentario_texto = models.TextField()
	comentario_fechahora = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['comentario_fechahora']

class Libro(models.Model):
	libro_num_registro = models.CharField(max_length = 6, default="0000-A")
	libro_titulo = models.CharField(max_length = 100)
	libro_autores = models.ManyToManyField(Autor)
	libro_editorial = models.ForeignKey(Editorial)
	libro_fecha_pub = models.DateField()
	libro_resumen = models.TextField(default="Resumen...")
	libro_comentarios = models.ManyToManyField(Comentario)
	
	def __unicode__(self):
		return self.libro_titulo
		
	class Meta:
		ordering = ['libro_titulo']
