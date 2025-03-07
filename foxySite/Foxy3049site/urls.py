from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('index.html', views.index, name="index"),
    path('games.html', views.games, name="games"),
    path('guestBook.html', views.guestbook, name="guestBook"),
    path('register.html', views.register, name="register"),
    path('reg/', views.reg, name="reg")
]
