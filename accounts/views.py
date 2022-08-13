from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import UserRegisterForm


# Signup view for user registration
class SignUpView(generic.CreateView):
    # used registration path because django built in path for registration
    template_name = 'registration/signup.html'
    # After user registration, redirect to Login page
    success_url = reverse_lazy('login')
    # Form for user registration
    form_class = UserRegisterForm
