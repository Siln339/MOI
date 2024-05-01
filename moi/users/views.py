from django.shortcuts import render
from . forms import Authorization_form

def loginView(request):
    return render(request, 'users/authorization.html')
