from django.urls import path

from .views import index

app_name = 'vid'

urlpatterns = [
    path('', index, name='index')
]