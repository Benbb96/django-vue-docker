from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    actors = models.ManyToManyField(Actor, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    grade = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
