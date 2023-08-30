from django.urls import path
from . import views

urlpatterns = [
    path('cake/', views.cake, name='cake')
]