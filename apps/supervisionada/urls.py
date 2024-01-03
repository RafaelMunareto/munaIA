from django.urls import path
from .controller import *

urlpatterns = [
    path('', supervisionada.index, name='supervisionada'),
]
