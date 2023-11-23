from client_app.views import *
from django.urls import path

urlpatterns = [
    path('', index,name="client_index"),
    path('create_project', create_project,name="create_project"),
]