from django.urls import path
from newform import views

urlpatterns = [
    path('', views.users, name='users')
]
