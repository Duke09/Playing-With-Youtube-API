from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/')
    template_name = 'registration/register.html'
