from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomeView, register

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('register/', register, name='RegisterView'),
    path('login/',
         auth_views.LoginView.as_view(template_name='home/login.html'),
         name='LoginView'),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='home/logout.html'),
         name='LogoutView'),
]
