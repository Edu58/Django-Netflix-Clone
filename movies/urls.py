from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/<movie_id>', views.play, name='play'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('search/', views.search, name='search'),
    path('profile/', views.profilePage, name='profile'),
    path('logout/', views.logoutUser, name='logout'),
]
