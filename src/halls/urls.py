from django.urls import path

from .views import (index, dashboard, Detail, 
                    CreateHall, DeleteHall, UpdateHall, 
                    create_video,)

app_name = 'halls'

urlpatterns = [
    path('', index, name='index'),
    # Hall URLS
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/hall/create/', CreateHall.as_view(), name='create'),
    path('dashboard/hall/detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('dashboard/hall/<int:pk>/update/', UpdateHall.as_view(), name='update'),
    path('dashboard/hall/<int:pk>/delete/', DeleteHall.as_view(), name='delete'),
    # Video URLS
    path('dashboard/hall/<int:pk>/create/video', create_video, name='create_video'),
]