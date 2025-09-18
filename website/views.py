from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    # Check to see if Logged In: [If a person is logging in they 'POST', 
    # otherwise they are going to the webpage and 'GET' stuff from that page]

    # If User is Posting:
    if request.method=='POST':
        # 'username' taken from home.html
        username=request.POST['username']
        password=request.POST['password']
        # Authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "home.html", {})  # ✅ add return here
    else:
        return render(request, "home.html", {})

# This function is not required as the login condition has already been defined in the home() function.
# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out...")
    return redirect('home')

def register_user(request):
    return render(request,"register.html",{})