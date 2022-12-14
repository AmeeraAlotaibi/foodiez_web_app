# Generated by Django 4.1 on 2022-08-13 14:45

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("Easy", "Easy"),
                            ("Medium", "Medium"),
                            ("Hard", "Hard"),
                        ],
                        max_length=15,
                    ),
                ),
                (
                    "duration",
                    models.DurationField(default=datetime.timedelta(seconds=1800)),
                ),
                (
                    "calories",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(10000),
                        ]
                    ),
                ),
                ("serving", models.PositiveIntegerField(default=1)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="static/images/placeholder.png",
                        upload_to="media/recipes/",
                    ),
                ),
                ("description", models.TextField()),
                ("directions", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="food.category",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        related_name="ingredients", to="food.ingredient"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="cat_ingredients", to="food.ingredient"
            ),
        ),
    ]
