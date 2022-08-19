from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from .models import Category, Ingredient, Recipe
from .forms import CategoryForm, IngredientForm, RecipeForm, RegisterForm, LoginForm
from django.forms import formset_factory


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
    return render(request, "snippets/register.html", context)

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
                return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "snippets/login.html", context)


# logging out view
def logout_view(request):
    logout(request)
    return redirect("home")


# home page view 
def home_view(request):
    recipes = Recipe.objects.all().order_by("-id")
    editors_pick = Recipe.objects.filter(editor_pick=True)
    categories = Category.objects.all()
    ingredients = Ingredient.objects.all()
    category_form = CategoryForm()
    ingredient_form = IngredientForm()
    context = {
        "recipes": recipes,
        "categories": categories,
        "category_form": category_form ,
        "editors_pick": editors_pick,
        "ingredient_form": ingredient_form,
        "ingredients": ingredients,
    }
    return render(request, "base.html", context)



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
                # this is to save the ingredients in the database
                form.save_m2m() 
                return redirect("home")
            else: 
                return redirect("forbidden")
    context = {
        "form": form,
    }
    return render(request, "pages/create_recipe.html", context)


# RECIPE DETAIL VIEW
def recipe_detail_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
   
    context = {
        "recipe": recipe,
    }
    return render(request, "pages/recipe_detail.html", context)


# DELETE RECIPE
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
    return render(request, 'pages/update_recipe.html', context)


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
    return render(request, 'snippets/add_cat.html', context)


# CATEGORY DETAILS
def category_details(request, cat_id):
    category = Category.objects.get(id=cat_id)
    context = {
        "category": category,
    }
    return render(request, "pages/cat_details.html", context)


# DELEETE CATEGORY
def delete_category(request, cat_id):
    cat = Category.objects.get(id=cat_id)
    cat.delete()
    return redirect("admin-page")


# ADD INGREDIENT
def create_ingredient(request):
    form = IngredientForm()
    if request.method == "POST":
        form = IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home") 
    
    context = {
        "form": form
    }
    return render(request, 'snippets/add_ing.html', context)


# DELETE INGREDIENT
def delete_ingredient(request, ing_id):
    ingredient = Ingredient.objects.get(id=ing_id)
    ingredient.delete()
    return redirect("admin-page")


# Admin page view - will adjust later 
def admin_view(request):
    categories = Category.objects.all()
    ingredients = Ingredient.objects.all()
    context = {
        "categories": categories,
        "ingredients": ingredients,
    }
    return render(request, 'pages/admin_page.html', context)



# FILTER RECIPES
def filter_recipes(request):
    all_recipes = Recipe.objects.all().order_by("-id")
    categories = request.GET.getlist("category[]")
    ingredients = request.GET.getlist("ingredient[]")
    levels = request.GET.getlist("difficulty[]")

    
    if len(categories) > 0:
        all_recipes = all_recipes.filter(category__id__in=categories)
    if len(ingredients) > 0:
        all_recipes = all_recipes.filter(ingredients__id__in=ingredients)
    if len(levels) > 0:
        all_recipes = all_recipes.filter(difficulty__in=levels)

    
    filter_template = render_to_string('ajax/recipes_list.html', {"data": all_recipes})

    return JsonResponse({"data": filter_template})



