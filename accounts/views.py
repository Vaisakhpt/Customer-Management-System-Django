from django.shortcuts import render,redirect
from .models import *
from .forms import OrderForm

def dashboard(request):
    customerr=Customer.objects.all()
    countc=customerr.count()
    orderr=Order.objects.all()
    counto=orderr.count()
    return render(request,'dashboard.html',{'countc':countc,'counto':counto,'customerr':customerr,'orderr':orderr})

def products(request):
    product=Product.objects.all()
    return render(request,'products.html',{'product':product})

def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orderr=customer.order_set.all()
    return render(request,'customer.html',{'customer':customer,'orderr':orderr})

def createOrder(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'orderform.html',{'form':form})

def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'orderform.html',{'form':form})

def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    return render(request,'delete.html',{'order':order})


