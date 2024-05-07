from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class AuthorizationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'input-field', 'placeholder':'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-field', 'placeholder':'Пароль'}))


class Registration_form(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ( 'email', 'username')

    def clean_password_repeat(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password_repeat']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cleaned_data['password_repeat']