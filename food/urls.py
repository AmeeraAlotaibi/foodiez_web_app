from django.urls import path
from food.views import admin_view, create_category, create_ingredient, create_recipe_view, delete_category, home_view, login_view, logout_view, recipe_detail_view, recipe_update, register_view, recipe_delete, filter_recipes

urlpatterns = [
    # LANDING PAGE HOME 
    path("", home_view, name="home"),
    # filter recipes using AJAX
    path("filter-recipes/", filter_recipes, name="filter-recipes"),
    # recipes
    path("create-recipe/", create_recipe_view, name="create-recipe"),
    path("recipe/<int:recipe_id>/", recipe_detail_view, name="recipe-detail"),
    path("delete/<int:recipe_id>/", recipe_delete, name="delete-recipe"),
    path("update/<int:recipe_id>/", recipe_update, name="update-recipe"),
    # categories
    path("create-category/", create_category, name="create-category"),
    path("delete/<int:cat_id>", delete_category, name="delete-category"),
    # ingredients
    path("create-ingredient/", create_ingredient, name="create-ingredient"),
    # USER AUTHENTICATION
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    # admin page for superusers and staff
    path("admin-page/", admin_view, name="admin-page"),
]
