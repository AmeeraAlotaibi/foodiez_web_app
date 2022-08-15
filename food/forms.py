
from django import forms 
from django.contrib.auth import get_user_model
from .models import Category, Ingredient, Recipe


User = get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        
        widgets = {
            "password": forms.PasswordInput()
        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput(),)
    

# CREATE A NEW RECIPE FORM
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['created_by', 'editor_pick']
    
    ingredients = forms.ModelMultipleChoiceField(
        queryset= Ingredient.objects.all(),
        widget= forms.CheckboxSelectMultiple
    )
    
    
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
      
        
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'