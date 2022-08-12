from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm


# Create your views here.
# registeration view
def register_view(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }
    
    return render(request, "register.html", context)

# loggin in view
def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                print("LOGGED IN-----------------------------")
                return redirect("home")
    context = {
        "form": form,
    }
    
    return render(request, "login.html", context)


# logging out view
def logout_view(request):
    logout(request)
    return redirect("home")


# home page view 
# add context later for all models
def home_view(request):
    return render(request, "landing_page.html")