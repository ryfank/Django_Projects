from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "accounts/home.html")

def xss_demo(request):
    return render(request, "accounts/xss_demo.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Create session
            return redirect("dashboard")  # Redirect to a protected page
        else:
            return render(request, "accounts/login.html", {"error": "Invalid credentials"})
    return render(request, "accounts/login.html")

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html", {"user": request.user})

def logout_view(request):
    logout(request)  # Destroy session
    return redirect("login")  # Redirect to login page

