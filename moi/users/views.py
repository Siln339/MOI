from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import AuthorizationForm, RegistrationForm
from django.urls import reverse_lazy

class AuthorizationView(LoginView):
    form_class = AuthorizationForm
    next_page = reverse_lazy('home')
    template_name = 'users/authorization.html'
    title = 'Вход'

def reistration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form, 'title':'Регистрация'})