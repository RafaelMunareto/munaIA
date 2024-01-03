from django.urls import path
from .controller import *

urlpatterns = [
    path('', controllers.index, name='home'),
    path('processar_base/', controllers.processar_base, name='processar_base'),
]
