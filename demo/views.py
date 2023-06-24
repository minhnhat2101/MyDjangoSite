from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import DemoUser
# Create your views here.
def home(request):
    users = DemoUser.objects.all()
    dictt = {'users':users}
    return render(request,"demo/index.html", dictt)



