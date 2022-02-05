from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm
from django.http import Http404, HttpResponse,JsonResponse
import time
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    customer_count = customers.count()
    order_count = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status='Pending').count()

    content = {
        'customers':customers, 'orders':orders,'cutomer_count':customer_count,
        'order_count':order_count,'delivered':delivered,'pending':pending
    }
    
    return render(request, "manipulations/dashboard.html", content)
   

   
def product(request):
    products = Product.objects.all()
    content = {
        'products':products
    }
    return render(request, "manipulations/products.html", content)

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    content = {
        'customer':customer,'orders':orders, 'order_count':order_count
    }

    return render(request, "manipulations/customer.html", content)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    content = {
        'form':form
    }
    return render(request, "manipulations/order_form.html", content)

def updateOrder(request, pk):
    order= Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    content = {
        'form':form
    }

    return render(request, "manipulations/order_form.html", content)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    content = {
        'order':order
    }        

    return render(request, "manipulations/delete_order.html", content)                   