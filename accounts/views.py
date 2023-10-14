from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == 'POST':
        # Get form values
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid credentials')
            return redirect('/accounts/login')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return redirect('/accounts/login')
        else:
            login(user)
            return redirect('/accounts/dashboard')
        
    return render(request, 'accounts/login.html')



def register(request):
    if request.method == 'POST':
        # Get form values
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')

        user=User.objects.filter(username=username).first()
        if user:
            messages.info(request, 'Username already exists')
            return render(request, 'accounts/register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name)
        

        user.set_password(password) # Hashing the password
        user.save()
        return render(request, 'accounts/login.html/')
        messages.success(request, 'Account created successfully')



    return render(request, 'accounts/register.html')

def logout_user(request):
    pass

def dashboard(request):
    return render(request, 'accounts/dashboard.html')