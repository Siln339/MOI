from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class AuthorizationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Пароль'}))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class':'authentification-form-input'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'authentification-form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'authentification-form-input'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'authentification-form-input'}))
    policy = forms.BooleanField(label='Согласие на обработку персональных данных', required=True, widget=forms.CheckboxInput(attrs={'class':'checkbox-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')