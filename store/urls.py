from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name="store"),
]
