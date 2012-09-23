import os

class DjangoServidor:
	def __init__(self):
		print "Iniciando servidor Django en local"
		self.iniciar_servidor()
		
	def iniciar_servidor(self):
		print "Conectando server"
		os.system('python manage.py runserver')
		
		
	def parar_servidor(self):
		print "Cerrando servidor"
