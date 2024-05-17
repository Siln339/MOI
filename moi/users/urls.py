from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.AuthorizationView.as_view(), name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('registration/', views.reistrationView, name='registration'),
]
