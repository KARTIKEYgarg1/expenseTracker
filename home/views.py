from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
def signup_view(request):
    if request.method=='POST':   
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.last_name = request.POST['income']
        user.save()
        return redirect('/')
    return render(request,'signup.html')

def login_view(request):
    if request.method=='POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.last_name is "111":
                return redirect('/home')
            else:
                prof=Profile(income=float(user.last_name), expense=0,balance=float(user.last_name),user=request.user)
                user.last_name = "111"
                user.save()
                prof.save()
                return redirect('/home')
        else:
            return render(request,'login.html',{'notLoggedIn':False,'invalidCredentials':True})
    return render(request,'login.html',{'notLoggedIn':False,'invalidCredentials':False})
def home(request):
    if request.user.is_authenticated:
        profile=Profile.objects.filter(user=request.user).first()
        expenses=Expense.objects.filter(user=request.user)
        if request.method=='POST':
            text=request.POST.get('text')
            amount=request.POST.get('amount')
            expensetype=request.POST.get('expensetype')
            expense=Expense(name=text, amount=amount,expense_type=expensetype,user=request.user)
            expense.save()
            if expensetype=='negative':
                profile.expense+=float(amount)
                profile.balance-=float(amount)
            else:
                profile.balance+=float(amount)
            profile.save()
            return redirect('/home')
        context={'profile':profile,'expenses':expenses}
        return render(request,'home.html',context)
    else:
        return render(request,'login.html',{'notLoggedIn':True,'invalidCredentials':False})
def logout_view(request):
    logout(request)
    return redirect('/')
