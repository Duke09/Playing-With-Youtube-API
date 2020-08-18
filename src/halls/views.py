from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, View, DetailView

from .models import Hall, Video

# Create your views here.
def index(request):
    return render(request, 'halls/index.html')

class Detail(DetailView):
    model = Hall
    template_name = 'halls/detail.html'

class Dashboard(View):
    template_name = 'halls/manage/dashboad.html'


class CreateView(CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/manage/create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateView, self).form_valid(form)
        return redirect('halls:index')

class UpdateView(View):
    pass

class DeleteView(View):
    pass