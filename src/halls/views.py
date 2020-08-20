from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .models import Hall, Video

# Create your views here.
def index(request):
    return render(request, 'halls/index.html')

def dashboard(request):
    halls = Hall.objects.all()
    return render(request, 'halls/manage/dashboard.html', {'halls':halls})


class CreateHall(CreateView):
    model = Hall
    fields = ['title']
    template_name = 'halls/manage/halls/create.html'
    success_url = reverse_lazy('halls:dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateView, self).form_valid(form)
        return redirect('halls:dashboard')

class Detail(DetailView):
    model = Hall
    template_name = 'halls/manage/halls/detail.html'

class UpdateHall(UpdateView):
    model = Hall
    template_name = 'halls/manage/halls/update.html'
    fields = ['title']
    success_url = reverse_lazy('halls:dashboard')

class DeleteHall(DeleteView):
    model = Hall
    template_name = 'halls/manage/halls/delete.html'
    success_url = reverse_lazy('halls:dashboard')

def create_video(request, pk):
    pass