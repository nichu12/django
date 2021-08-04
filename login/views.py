from django.core.checks import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render
import datetime

from .models import Login
from login import models
# Create your views here.
def main(request):
   time = datetime.date.today()
   return render(request,'ind.html',{'time':time})


@login_required(login_url='/login')
def homepage(request):
   print(request.user)
   return render(request, 'home.html')   

def login(request):
   print(request.user)
   if request.method == 'POST': 
      name = request.POST['name']
      passw = request.POST['password']

      usera = auth.authenticate(username=name,password=passw)

      if usera is not None:
         auth.login(request,usera)
         return redirect('/homepage',{'name':name})
      else:
         messages.info(request,'invalid credential')   
         return redirect('/login')
   else:
      return render(request,"login.html")    

def register(request):
   if request.method == 'POST':
      name = request.POST['name']
      passw = request.POST['password']
      f_name = request.POST['first_name']
      l_name = request.POST['last_name']
      mail = request.POST['email']

      if User.objects.filter(username=name).exists():
         messages.info(request,'Username Exists')
         return redirect('/register')
      elif User.objects.filter(email=mail).exists():
         messages.info(request,'User already registered with this Email')
         return redirect('/register')    
      else:
         user = User.objects._create_user(username=name,password=passw,first_name=f_name,last_name=l_name,email=mail)
         user.save();
         print('user created')
         return redirect('/')   
   else:
      return render(request,"index.html")   
