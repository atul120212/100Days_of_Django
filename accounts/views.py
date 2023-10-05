from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    return render(request, 'accounts/register.html')

def logout_user(request):
    pass

def dashboard(request):
    return render(request, 'accounts/dashboard.html')