from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from app.models import grocery_item

def home(request):
    item_list=grocery_item.objects.filter(user_name=request.user.username)
    context={ 'item_list':item_list }
    return render(request,'home.html',context)

def update_item(request,pk):
    if request.method=='POST':
        obj=grocery_item.objects.filter(id=pk)[0]
        obj.item_name=request.POST['item_name']
        obj.item_quantity=request.POST['item_quantity']
        obj.item_status=request.POST['item_status']
        obj.item_date=request.POST['item_date']
        obj.user_name=request.user.username
        obj.save()
        return redirect('/')
    else:
        item=grocery_item.objects.filter(pk=pk)[0]
        context={'item':item,'pk':pk}
        return render(request,'update_item.html',context)

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        email=request.POST['email'] 
        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('/register')
            elif User.objects.filter(username=username).exists():
                messages.error(request,'Username Already Exists')
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('/login')
        else:
            messages.error(request,'Password Not Matching, Try Again')
            return redirect('/register')
    else:
        return render(request,'register.html')

def login_request(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid User Name or Password')
            return redirect('/login')
    return render(request,'login_request.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/")

def add_item(request):
    if request.method=='POST':
        item_name=request.POST['item_name']
        item_quantity=request.POST['item_quantity']
        item_status=request.POST['item_status']
        item_date=request.POST['item_date']
        user_name=request.user.username
        obj1=grocery_item.objects.create(item_name=item_name,item_quantity=item_quantity,item_status=item_status,item_date=item_date,user_name=user_name)
        obj1.save()
        return redirect('/')
    else:
        return render(request,'add_item.html')

def delete_item(request,pk):
    grocery_item.objects.filter(pk=pk).delete()
    return redirect('/')

def filter_date(request):
    item_list=grocery_item.objects.filter(user_name=request.user.username,item_date=request.POST['filter_date'])
    context={ 'item_list':item_list }
    return render(request,'home.html',context)

