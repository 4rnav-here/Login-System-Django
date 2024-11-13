from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')
        
        if User.objects.filter(username=username):
            messages.error(request,"User already exists")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered")
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
        
        if not username.isalnum():
            messages.error(request, "The username should be alpha numeric")
            return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        
        messages.success(request, "Your account has been successfully created")
        
        subject = "Welcome to this django application"
        message = "Hello" + myuser.first_name + "!! \n" + "Welcome to my project!! \n Thank u for visitng this project.~"
        
        
        
        
        
        
        print("User created successfully, redirecting to signin...")  # Debug statement
        return redirect('signin')  # Ensure this is a URL pattern name, not a template name
    
    return render(request, "authentication/signup.html")

        
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user) 
            fname = user.first_name
            return render(request, "authentication/index.html", {'fname':fname})
        else:
            messages.error(request, "Wrong credentials entered")
            return redirect('home')
            
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')