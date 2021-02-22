from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField
from django.core.exceptions import ObjectDoesNotExist

preference_choices = (
    ("Adventure", "Adventure"),
    ("Architecture", "Architecture"),
    ("Historical", "Historical"),
    ("Religious", "Religious"),
    ("Educational", "Educational"),
    ("Trekking", "Trekking"),
    ("Sightseeing", "Sightseeing"),
    ("Cultural", "Cultural"),
    ("Wildlife", "Wildlife"),
    ("One-Day-Trip", "One-Day-Trip")
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferences  = MultiSelectField(choices= preference_choices, default=(1,"Adventure"))

    def __str__(self):
        return f'{self.user.username} Profile'
    

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)
    