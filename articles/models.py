from django.db import models
from multiselectfield import MultiSelectField

preference_choices = (
    ("1", "Adventure"),
    ("2", "Relaxation"),
    ("3", "Nature"),
    ("4", "Architecture"),
    ("5", "Historical"),
    ("6", "Religious")
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
    tags = MultiSelectField(choices= preference_choices, default=("1","Adventure"))
    # add author name

    def __str__(self):
        return self.title

    # To only display 350 characters in frontend
    def snippet(self):
        return self.body[:350] + '...'
