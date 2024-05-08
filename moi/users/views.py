from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import AuthorizationForm, RegistrationForm
from django.urls import reverse_lazy
from django.shortcuts import render

class AuthorizationView(LoginView):
    form_class = AuthorizationForm
    next_page = reverse_lazy('')
    template_name = 'users/authorization.html'
    title = 'Вход'

class RegistrationView(CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('')
    template_name = 'users/registration.html'
    title = 'Регистрация'