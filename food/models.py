from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.name
    


class Recipe(models.Model):
    
    difficulty_choices = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    directions = models.TextField()
    image = models.ImageField() # add a default image in static files
    time = models.TimeField()
    serving = models.PositiveIntegerField(default=1)
    difficulty = models.CharField(choices=difficulty_choices, max_length=15)
    calories = models.FloatField()
    rating = models.FloatField() 
    hand_picked = models.BooleanField(default=False)
    
    
    def __str__(self) -> str:
        return self.name
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recipes = models.ManyToManyField(Recipe, related_name="recipe")
    categories = models.ManyToManyField(Category ,related_name="category")
    
    def __str__(self) -> str:
        return self.name
    