from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Recipe

@receiver(post_save, sender=Recipe)
def get_created_by(instance, sender, created, **kwargs):
    if created == True:
        instance.created_by = instance.request.user
        instance.save()