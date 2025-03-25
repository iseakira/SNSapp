from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import BoardModel

# Create your views here. 
def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html')
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録済みです'})

    return render(request,'signup.html')


def Loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request,'login.html',{'context':'login success'})
        else:
            return render(request,'login.html',{'context':'not logged in'})
        
    return render(request,'login.html',{'context':'get'})

def Listfunc(request):
    object_list = BoardModel.objects.all()
    return render(request,'list.html',{'object_list':object_list})
    