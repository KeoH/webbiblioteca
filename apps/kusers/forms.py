#encoding: utf-8
from django import forms
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        label='Nombre de usuario',
        label_suffix='',
        error_messages = {
            'required' : 'Es necesario el nombre de usuario',
            'invalid_user' : 'Usuario no reconocido',
        },
        widget = forms.TextInput(
            attrs = {
                'class' : 'textinput',
                'placeholder' : 'Introduce tu nombre de usuario'
            }
        )
    )
    password = forms.CharField(
        required=True,
        label='Contraseña',
        label_suffix='',
        error_messages = {
            'required' : 'Es necesaria la contraseña',
            'invalid_password' : 'Contraseña incorrecta',
        },
        widget = forms.PasswordInput(
            attrs = {
                'class' : 'passinput',
                'placeholder' : 'Introduce la contraseña'
            }
        )
    )

    user_cache = None

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.user_cache = authenticate(username=username, password=password)

        if self.user_cache is not None:
            if self.user_cache.is_active:
                return self.cleaned_data
            else:
                raise forms.ValidationError("Usuario inactivo")
        else:
            raise forms.ValidationError("Usuario incorrecto")

    def get_user(self):
        return self.user_cache
