from django.db import models

# Create your models here.
class DemoUser(models.Model):
  id = models.AutoField(primary_key=True)
  username = models.CharField(max_length=50, blank=False)
  password = models.CharField(max_length=50, blank=False)
  
