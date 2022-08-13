from socket import fromshare
from django import forms 
from django.contrib.auth import get_user_model
from .models import Recipe


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
        exclude = ['created_by']