#encoding:utf-8
#from .models import UserProfile
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

class UserLoginForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

	def __init__(self, *args, **kwargs):
		self.user_cache = None
		super(UserLoginForm, self).__init__(*args, **kwargs)

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		self.user_cache = authenticate(username=username, password=password)

		if self.user_cache is None:
			raise forms.ValidationError(_('Incorrect user'))
		elif not self.user_cache.is_active:
			raise forms.ValidationError(_('Inactive user'))

		return self.cleaned_data

	def get_user(self):
		return self.user_cache