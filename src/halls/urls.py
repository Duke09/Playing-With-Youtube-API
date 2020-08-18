from django.urls import path

from .views import Dashboard, DeleteView, Detail, UpdateView, index, CreateView

app_name = 'halls'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dashboard/hall/create/', CreateView.as_view(), name='create'),
    path('dashboard/hall/<int:pk>/update/', UpdateView.as_view(), name='update'),
    path('dashboard/hall/<int:pk>/delete/', DeleteView.as_view(), name='delete'),
]