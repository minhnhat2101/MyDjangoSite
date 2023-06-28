from django.contrib import admin
from django.urls import path
from demo import views

urlpatterns = [
    path('', views.home, name="demo"),
    path('result/', views.check1, name='login'),
    path('regis/', views.register, name='regis'),

]
