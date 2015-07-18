from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView, View
from django.shortcuts import render
from .models import Kuser

from django.contrib.auth import login, logout
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from core.views import LoginRequiredMixin

class UserPublicProfileView(DetailView):
    model = Kuser
    template_name = "profile.html"

class UserPublicProfileListView(ListView):
    model = Kuser
    context_object_name = 'users'
    template_name = "profile-list.html"

class UserDashboard(LoginRequiredMixin, View):

    template_name = "user-dashboard.html"
    ctx = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.ctx)


class UserLogin(View):

    template_name = "user-login.html"
    ctx = {}

    def get(self, request):
        self.ctx['form'] = LoginForm()
        return render(request, self.template_name, self.ctx)

    def post(self, request):
        self.ctx['form'] = LoginForm(request.POST)
        if self.ctx['form'].is_valid():
            login(request, self.ctx['form'].get_user())
            return HttpResponseRedirect(reverse('users:user-dashboard'))
        return render(request, self.template_name, self.ctx)

class UserLogout(LoginRequiredMixin, View):

    template_name = "user-logout.html"
    ctx = {}

    def get(self, request):
        logout(request)
        return render(request, self.template_name, self.ctx)
