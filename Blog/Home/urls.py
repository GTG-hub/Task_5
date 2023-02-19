from django.contrib import admin
from django.urls import path, include
from Home import views
from .views import *
urlpatterns = [
    path('',views.index,name="Home"),
    path('login/', views.login, name="login")
]
