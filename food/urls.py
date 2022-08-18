from django.urls import path
from food import views

urlpatterns = [
    # LANDING PAGE HOME 
    path("", views.home_view, name="home"),
    # filter recipes using AJAX
    path("filter-recipes/", views.filter_recipes, name="filter-recipes"),
    # recipes
    path("create-recipe/", views.create_recipe_view, name="create-recipe"),
    path("recipe/<int:recipe_id>/", views.recipe_detail_view, name="recipe-detail"),
    path("delete/<int:recipe_id>/", views.recipe_delete, name="delete-recipe"),
    path("update/<int:recipe_id>/", views.recipe_update, name="update-recipe"),
    # categories
    path("create-category/", views.create_category, name="create-category"),
    path("delete-category/<int:cat_id>/", views.delete_category, name="delete-category"),
    path("category-details/<int:cat_id>", views.category_details, name="category-details"),
    # ingredients
    path("create-ingredient/", views.create_ingredient, name="create-ingredient"),
    path("delete-ingredient/<int:ing_id>/", views.delete_ingredient, name="delete-ingredient"),
    # USER AUTHENTICATION
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # admin page for superusers and staff
    path("admin-page/", views.admin_view, name="admin-page"),
]

