from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import AddCustomer
from .forms import CustomerForm
from django.core.paginator import Paginator
# Create your views here.

def add_customer(request):
  return render(request, 'customer/add-customer.html')

def list_customer(request):
  data = AddCustomer.objects.all()
  paginator = Paginator(data,10)
  page_number = request.GET.get('page_number')
  page_obj = paginator.get_page(page_number)
  return render(request,'customer/list-customer.html',{'page_obj':page_obj})

def add_new_customer(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    context = AddCustomer(name= name,phone= phone,address= address)
    context.save()
  data = AddCustomer.objects.all()
  paginator = Paginator(data,10)
  page_number = request.GET.get('page_number')
  page_obj = paginator.get_page(page_number)
  return render(request,'customer/list-customer.html',{'page_obj':page_obj})


def update_customer(request, customer_id):
  customer = get_object_or_404(AddCustomer, id=customer_id)
  context = {'customer':customer}
  return render(request,'customer/update-customer.html',context)

def update_process(request):
  if request.method == 'POST':
    id = request.POST.get('customer_id')
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    AddCustomer.objects.filter(id=id).update(name= name,phone= phone,address= address)
    data = AddCustomer.objects.all()
    context = {'data': data}
    return render(request,'customer/list-customer.html',context)

def delete_cus(request,customer_id):
  customer = get_object_or_404(AddCustomer, id=customer_id)
  context = {'customer':customer}
  return render(request,'customer/delete-customer.html',context)

def delete_process(request):
  if request.method == 'POST':
    id = request.POST.get('customer_id')
    AddCustomer.objects.filter(id=id).delete()
    data = AddCustomer.objects.all()
    context = {'data': data}
    return render(request,'customer/list-customer.html',context)

def delele_customer(request):
  if request.method == 'GET':
    customer_id = request.GET['customer_id']
    customer = AddCustomer.objects.get(id = customer_id)
    customer.delete()
    context = {
        'mess' :"Xóa thành công"
    }
  return JsonResponse(context)
