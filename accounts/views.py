from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CustomerForm
from .forms import OrderForm
from .filters import OrderFilter
from .decorators import allowed_users

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    customerr=Customer.objects.all()
    countc=customerr.count()
    orderr=Order.objects.all()
    counto=orderr.count()
    return render(request,'dashboard.html',{'countc':countc,'counto':counto,'customerr':customerr,'orderr':orderr})

@login_required(login_url='loginpage')
def products(request):
    product=Product.objects.all()
    return render(request,'products.html',{'product':product})

@login_required(login_url='loginpage')
def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    orderr=customer.order_set.all()
    myFilter=OrderFilter(request.GET,queryset=orderr)
    orderr=myFilter.qs
    return render(request,'customer.html',{'customer':customer,'orderr':orderr,'myFilter':myFilter})

@login_required(login_url='loginpage')
def createOrder(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'orderform.html',{'form':form})

@login_required(login_url='loginpage')
def updateOrder(request,pk):
    order=Order.objects.get(id=pk)
    form=OrderForm(instance=order)
    if request.method=='POST':
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request,'orderform.html',{'form':form})

@login_required(login_url='loginpage')
def deleteOrder(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('dashboard')
    return render(request,'delete.html',{'order':order})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('loginpage')
    return render(request,'loginpage.html')

def registerPage(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('loginpage')
    return render(request,'registerpage.html',{'form':form})


def logoutPage(request):
    if request.method=='POST':
        logout(request)
        return redirect('loginpage')

@login_required(login_url='loginpage')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    customer=request.user.customer
    orderr=customer.order_set.all()
    myFilter=OrderFilter(request.GET,queryset=orderr)
    orderr=myFilter.qs
    return render(request,'userpage.html',{'customer':customer,'orderr':orderr,'myFilter':myFilter})

def customerSettings(request):
    customer=request.user.customer
    form=CustomerForm(instance=customer)
    if request.method=='POST':
        form=CustomerForm(request.POST,request.FILES,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('userpage')
    return render(request,'customerform.html',{'form':form})



        


