from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/<movie_id>', views.play, name='play')
]
