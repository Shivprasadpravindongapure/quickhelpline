from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# ---------- Homepage ----------
def home(request):
    return render(request, 'users/home.html')

# ---------- Dashboard ----------
def dashboard(request):
    # Only logged-in users can see dashboard
    if not request.user.is_authenticated:
        messages.error(request, "You must login first")
        return redirect('login')
    return render(request, 'users/dashboard.html')

# ---------- Register ----------
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'User registered successfully')
        return redirect('login')

    return render(request, 'users/register.html')

# ---------- Login ----------
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    return render(request, 'users/login.html')

# ---------- Logout ----------
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')
