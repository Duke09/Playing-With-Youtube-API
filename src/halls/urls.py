from django.urls import path

from .views import index, CreateHall

app_name = 'halls'

urlpatterns = [
    path('', index, name='index'),
    path('vid/create/', CreateHall.as_view(), name='create_vid')
]