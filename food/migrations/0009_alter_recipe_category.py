# Generated by Django 4.1 on 2022-08-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0008_category_ingredients_remove_recipe_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="category",
            field=models.ManyToManyField(related_name="categories", to="food.category"),
        ),
    ]
