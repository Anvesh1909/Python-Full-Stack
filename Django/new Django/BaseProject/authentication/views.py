from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages

# ✅ Register View
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'register.html')

        # Validate password
        try:
            validate_password(password)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)
            return render(request, 'register.html')

        # Create user and login
        try:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f"Unexpected error: {e}")
            return render(request, 'register.html')

    return render(request, 'register.html')


# ✅ Login View
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')


# ✅ Logout View
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')


# ✅ Dashboard View (Protected)
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
