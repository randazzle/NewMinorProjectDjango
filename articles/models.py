from django.db import models
from multiselectfield import MultiSelectField

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
class Article(models.Model):
    title= models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    body1 = models.TextField()
    body2 = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.jpg', blank = True)
    img1 = models.ImageField(default = 'default.jpg', blank = True)
    img2 = models.ImageField(default = 'default.jpg', blank = True)
    tags = MultiSelectField(choices= preference_choices, default=(1, "Adventure"), blank=False)
    # add author name

    def __str__(self):
        return self.title

    # To only display 350 characters in frontend
    def snippet(self):
        return self.body[:350] + '...'
