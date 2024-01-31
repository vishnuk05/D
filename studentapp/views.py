from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import addform
from .models import signup
from django.contrib.auth import authenticate, login as log, logout

# Create your views here.

def home(request):
    form=addform()
    if request.method=="POST":
        form=addform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,"signup.html",{'form':form})


def view(request):
    cr = signup.objects.all()
    return render(request,'view.html', {'cr': cr})


#delete
def delete(request,pk):
    de = signup.objects.get(id=pk)
    de.delete()
    return redirect('view')

# update
def update(request,pk):
    up =signup.objects.get(id=pk)
    form =addform(instance=up)
    if request.method =="POST":
        form =addform(request.POST, instance=up)
        if form.is_valid():
            form.save()
            return redirect('view')
    return render(request,'update.html',{'form':form})

def udpateuser(request):
    return render(request,'update.html')


# loginpage
def login(request):
    return render(request,'login.html')
# logout
def userlogout(request):
    logout(request)
    return redirect('login')

# 
def welcome(request):
    id=request.session['id']
    username=request.session['username']
    profile=signup.objects.get(pk=id)
    return render(request,'welcome.html',{'id':id,'username':username,'profile':profile})

# login page validation
def validate(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password= request.POST.get('password')
        cr = signup.objects.filter(username=username,password=password)
        if cr:
            userdetails =signup.objects.get(username=username,password=password)
            id= userdetails.id
            username= userdetails.username
            request.session['id']=id
            request.session['username']=username
            request.session['password']=password
            
            return redirect('welcome')
        else:
            invalid='invalid credentials'
            return render(request,'login.html',{'invalid':invalid})
    else:
        return redirect('home')