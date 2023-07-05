from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.
class AddCustomer(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=250)
  phone = models.CharField(max_length=250)
  address = models.CharField(max_length=250)

class CustomerForm(forms.Form):
  name = forms.CharField(max_length=250)
  phone = forms.CharField(max_length=250)
  address = forms.CharField(max_length=250)

