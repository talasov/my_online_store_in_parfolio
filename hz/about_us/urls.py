from django.urls import path
from .views import *

urlpatterns = [
    path('certificate/', certificate, name='certificate'),
    path('contract/', contract, name='contract'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
]