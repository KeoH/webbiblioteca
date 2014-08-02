from .forms import UserLoginForm
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

class Log_In(View):

	def get(self, request):
		form = UserLoginForm()
		ctx = {'form_signin':form}
		return render(request, "fulllogin.html", ctx)

	def post(self, request):
		form = UserLoginForm(request.POST)
		errors = "Errores en el formulario"
		ctx = {'form_signin':form, 'errors':errors}
		if form.is_valid():
			login(request, form.get_user())
			return HttpResponseRedirect(reverse('home'))
		return render(request, "fulllogin.html", ctx)

class Log_Out(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse('home'))