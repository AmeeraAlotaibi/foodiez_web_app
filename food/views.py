from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import Category, Recipe
from .forms import CategoryForm, RecipeForm, RegisterForm, LoginForm


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
            messages.success(f"Account created for {user}")
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
    form = LoginForm()
    register = RegisterForm()
    recipes = Recipe.objects.all()
    editors_pick = Recipe.objects.filter(editor_pick=True)
    categories = Category.objects.all()
    category_form = CategoryForm()
    context = {
        "form": form,
        "register": register,
        "recipes": recipes,
        "categories": categories,
        "category_form": category_form ,
        "editors_pick": editors_pick,
    }

    return render(request, "base.html", context)


# USER FORBIDDEN PAGE
def forbidden_view(request):
    form = LoginForm()
    register = RegisterForm()
    
    context = {
        "form": form,
        "register": register,
    }
    
    return render(request, 'forbidden.html', context)



# CREATING A RECIPE VIEW
def create_recipe_view(request):
    form = RecipeForm()
    
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            if request.user.is_authenticated:
                recipe.created_by = request.user
                recipe.save()
                form.save_m2m() 
                return redirect("home")
            else: 
                return redirect("forbidden")
    
    context = {
        "form": form,
    }
    
    return render(request, "create_recipe.html", context)


# RECIPE DETAIL VIEW
def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
   
    context = {
        "recipe": recipe,
    }
    
    return render(request, "recipe_detail.html", context)

# DELETE RECIPE
# AUTHENTICATION HAPPENS IN TEMPLATE
def recipe_delete(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect("home")


# UPDATE RECIPE INFO
def recipe_update(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(instance=recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("home")
    context = {
        "recipe": recipe,
        "form": form,
    }
    return render(request, 'update_recipe.html', context)


# CREATE NEW CATEGORY
def create_category(request):
    form = CategoryForm()     
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    
    context = {
        "form": form,
    }
    return render(request, 'add_cat.html', context)


# DELEETE CATEGORY
def delete_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    cat.delete()
    return redirect("home")


