from django.contrib.auth.views import LoginView
from .forms import AuthorizationForm
from django.urls import reverse_lazy

class AuthorizationView(LoginView):
    form_class = AuthorizationForm
    next_page = reverse_lazy('login')
    template_name = 'users/authorization.html'
    title = 'Вход'