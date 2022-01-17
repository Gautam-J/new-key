from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


class HomeView(TemplateView):
    template_name = 'home/home.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('LoginView')
    else:
        form = UserRegisterForm()
    return render(request, 'home/register.html', {'form': form})
