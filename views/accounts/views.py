from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.apps import apps
from django.http import HttpResponseRedirect

from .forms import SignUpForm

# Create your views here.

# class LoginView(FormView)
# GET - отдает форму с запросом логина и пароля
# POST - генерирует сессию: отдавая ее ползователю


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'accounts/signup.html'


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_field_name = 'next' # default
    extra_context = {'key': 'value'}
    authentication_form = AuthenticationForm # default


# LogoutView(TemplateView)
class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    # next_page =
    redirect_field_name = 'next'
    extra_context = {}


# PasswordChangeView(FormView)
class UserPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    # success_url = reverse('password_change_done') default
    extra_context = {}
    # form_class = PasswordChangeForm default


# PasswordChangeDoneView(TemplateView)
class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
    extra_context = {} # title


class UserPermissions(TemplateView):
    template_name = 'accounts/custom_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Ваши разрешения'
        context['data'] = self.request.user.get_all_permissions()
        return context

