from django.contrib import admin
from .models import DemoUser
# Register your models here.

@admin.register(DemoUser)
class DemoUserAdmin(admin.ModelAdmin):
  list_display = ["id", "username", "password"]
  list_display_links = ["username", "password"]  
  list_filter = ["username"]
