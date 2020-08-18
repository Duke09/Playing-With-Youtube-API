from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView

from .models import Hall, Video

# Create your views here.
def index(request):
    return render(request, 'halls/index.html')

class CreateHall(CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/manage/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateHall, self).form_valid(form)
        return redirect('halls:index')