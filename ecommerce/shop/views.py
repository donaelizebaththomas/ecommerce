from django.shortcuts import render,redirect
from shop.models import category,product
# to register user
from django.contrib.auth.models import User
# for authentication validation
from django.contrib.auth import authenticate,login,logout
# to pass value in text
from django.http import HttpResponse
# Create your views here.

#   For displaying all Categories

def allcategories(request):
    """ Display all Categories in home page"""
    c=category.objects.all()
    return render(request,'category.html',{'category':c})

# For displaying products under a particular category

def allproducts(request,p):
    """ Display the product details """
    c=category.objects.get(id=p)
    p=product.objects.filter(Category=p)
    return render(request,'product.html',{'c':c,'p':p})

def showdetail(request,p):
    p=product.objects.get(id=p)
    return render(request,'detail.html',{'p':p})

def register(request):
    """  register a new user in django User table """
    if (request.method == "POST"):  # Check if the form is submitted
        u = request.POST['username']
        p = request.POST['password']
        cp = request.POST['confirmpassword']
        e=request.POST['email']
        fn=request.POST['firstname']
        ln=request.POST['lastname']
        if(cp==p):
            user = User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln,)
            user.save()
            return redirect('shop:allcat')
        else:
            return HttpResponse("Password are not the same")
    return render(request,'Register.html')

def user_login(request):
    """ login validation code in django """
    if(request.method=="POST"):
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        """ checking the user name and password correct or not """
        if User:
            login(request,user)
            return redirect('shop:allcat')
        else:
            return HttpResponse("Invalid Credintial")
    return render(request,'Login.html')


def user_logout(request):
    """ user logout function """
    logout(request)
    return user_login(request)