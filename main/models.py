from django.db import models
from django.contrib.auth.models import AbstractUser

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class User(AbstractUser):
    nickname = models.CharField(max_length=255, blank=True)
    
    class Meta:
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return self.username


class Recipe(models.Model):
    DIFFICULTY_LEVELS = (
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    )
    name = models.CharField(max_length=120)
    ingredients = models.CharField(max_length=400)
    picture = models.FileField()
    difficulty = models.CharField(choices=DIFFICULTY_LEVELS, max_length=10)
    prep_time = models.PositiveIntegerField()
    prep_guide = models.TextField()
    tags = models.ManyToManyField(Tag)
    users_favorited = models.ManyToManyField(User, related_name='favorited_recipes')

    def __str__(self):
        return "Recipe for {}".format(self.name)







