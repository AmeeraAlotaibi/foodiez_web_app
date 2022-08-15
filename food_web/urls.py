"""food_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from food.views import create_category, create_recipe_view, delete_category, forbidden_view, home_view, login_view, logout_view, recipe_detail_view, recipe_update, register_view, recipe_delete, forbidden_view

urlpatterns = [
    path("admin/", admin.site.urls),
    # LANDING PAGE HOME 
    path("", home_view, name="home"),
    path("create-recipe/", create_recipe_view, name="create-recipe"),
    path("recipe/<int:recipe_id>/", recipe_detail_view, name="recipe-detail"),
    path("delete/<int:recipe_id>/", recipe_delete, name="delete-recipe"),
    path("update/<int:recipe_id>/", recipe_update, name="update-recipe"),
    path("create-category/", create_category, name="create-category"),
    path("delete/<int:cat_id>", delete_category, name="delete-category"),
    # USER AUTHENTICATION
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    # if the user tries to create without loggin in
    path("forbidden/", forbidden_view, name="forbidden"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
