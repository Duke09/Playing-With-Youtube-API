from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
class Registration(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('halls:index')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        view = super(Registration, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view