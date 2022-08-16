from multiprocessing import context
from django.shortcuts import render , HttpResponse,redirect
from django.contrib.auth.forms import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from .models import extendeduser
# Create your views here.
def home(request):
    return render(request,"home.html")

def signup(request):
   if request.method == "POST":
      name = request.POST.get("name") 
      username = request.POST.get("username")
      email =  request.POST.get("email")
      aadhaarno = request.POST.get("aadhaarnumber")
      password = request.POST.get("password")
      confirmpassword = request.POST.get("confirmpassword")
      if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')
        
      if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')
        
      if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('home')
        
      if password != confirmpassword:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')
        
      if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')  
      myuser = User.objects.create_user(username,email,password)
      myuser.save()
      signup = extendeduser(name = name,email = email,username = username,aadhaar_no = aadhaarno,password=password)
      signup.save()
     
      messages.success(request,"your account has been successfully created")
      return redirect('signin')
      
   return render(request,"signup.html")

def signin(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      
      user = authenticate(username=username,password=password)
      if user is not None:
         login(request,user)
         return render(request,"about.html")
      else:
         return redirect(signin)
   return render(request,"signin.html")

def about(request):
    return render(request,"about.html")