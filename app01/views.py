from app01 import models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,reverse


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user = models.UserInfo.objects.create_user(username=username,password=password,phone=phone)
        print(user)
        return redirect(reverse('login'))
    return render(request,'register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = auth.authenticate(request,username=username,password=password)
        print(user_obj)
        if user_obj:
            auth.login(request,user_obj)
            return redirect(reverse('app01:index'))
    return render(request,'login.html')

@login_required
def index(request):

    return render(request,'index.html')

def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))

