from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import UserRegisterForm


class SignUpView(generic.CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm
    success_message = 'Account created successfully'
