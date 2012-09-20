from libreria.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import send_mail

def contacto(request):
	
	errors=[]
	if request.method == 'POST':
		if not request.POST.get('asunto', ''):
			errors.append('Introduce un asunto para el e-mail')
		if not request.POST.get('mensaje', ''):
			errors.append('Escribe algo en el cuerpo del mensaje')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Introduce una direccion de e-mail valida')
		if not errors:
			send_mail(
				request.POST['asunto'],
				request.POST['mensaje'],
				request.POST.get('email', 'noemail@example.com'),
				['keoh77@gmail.com'],
			)
			return HttpResponseRedirect('/')
	return render_to_response('contacto.html',{'errors':errors})
