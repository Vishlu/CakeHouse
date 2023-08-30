from django.urls import path
from . import views

urlpatterns = [
    path('owner/', views.author, name='author')
]