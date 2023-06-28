from django.db import models
from django import forms

# Create your models here.
class DemoUser(models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50, blank=False)
  password = models.CharField(max_length=50, blank=False)
  
class ExampleForm(forms.Form):
  user_name = forms.CharField(label='User name',min_length=5, max_length=100)
  password = forms.CharField(label='Password', widget=forms.PasswordInput)
  remember = forms.BooleanField(label = "Remember me")
