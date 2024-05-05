from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class AuthorizationView(LoginView):
    form_class = AuthenticationForm
    next_page = reverse_lazy('login')
    template_name = 'users/authorization.html'
    title = 'Вход'