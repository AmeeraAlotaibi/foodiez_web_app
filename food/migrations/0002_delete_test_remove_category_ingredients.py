# Generated by Django 4.1 on 2022-08-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Test",
        ),
        migrations.RemoveField(
            model_name="category",
            name="ingredients",
        ),
    ]
