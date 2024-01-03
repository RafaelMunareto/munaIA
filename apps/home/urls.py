from django.urls import path
from .views import *

urlpatterns = [
    path('', home.listar, name='home'),
]
