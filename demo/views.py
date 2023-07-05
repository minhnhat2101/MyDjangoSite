from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import ExampleForm

# Create your views here.
def home(request):
    form = ExampleForm()
    context = {'form':form}
    return render(request,"demo/index.html", context)

def check1(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            username = request.POST.get('user_name')
            pass1 = request.POST.get('password')
            context = {
                "user": username,
                "pass": pass1
            }
            return render(request,"demo/result.html", context)
        else:
            form = ExampleForm()
            context = {'form':form}
            return render(request,'demo/index.html',context)
                

def register(request):
    return render(request,'demo/regis.html')

