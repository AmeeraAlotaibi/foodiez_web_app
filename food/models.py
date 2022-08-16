from datetime import timedelta
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

User = get_user_model()

    
class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self) -> str:
        return self.name

# There is a relationship missing between the ingredient and the category, according to the trello board,
# refer to ---> As a user, I can see all the ingredients that belong to a category
# This means that every time an ingredient is created, a relationship between said ingredient is established with a category
# Im certain you are going to manage to integrate this type of relationship into to project
# This should be a priority over working on the search functionality with ajax
class Recipe(models.Model):
    
    difficulty_choices = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    name = models.CharField(max_length=200)
    difficulty = models.CharField(choices=difficulty_choices, max_length=15)
    duration = models.DurationField(default= timedelta(minutes=30))
    calories = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    serving = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE ,related_name="category")
    ingredients = models.ManyToManyField(Ingredient, related_name="ingredients")
    image = models.ImageField(upload_to="recipes/", default= "static/placeholder.png") # add a default image in static files
    description = models.TextField()
    directions = models.TextField()
    editor_pick = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name
    
