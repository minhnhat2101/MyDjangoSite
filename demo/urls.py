from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('', views.home, name="demo"),
    path('sum/', sum, name='sum'),
]
