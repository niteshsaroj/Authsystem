from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signup successful.")
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
