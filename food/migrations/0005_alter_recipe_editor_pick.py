# Generated by Django 4.1 on 2022-08-15 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0004_recipe_editor_pick_alter_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="editor_pick",
            field=models.BooleanField(default=False),
        ),
    ]
