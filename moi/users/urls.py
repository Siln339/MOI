from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AuthorizationView.as_view(), name='login'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
