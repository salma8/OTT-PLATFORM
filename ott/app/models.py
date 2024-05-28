from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)
    director = models.TextField(blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='static/movies')
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title


class Customer(models.Model):
    FirstName = models.TextField(max_length=100)
    LastName = models.TextField(max_length=100)
    Email = models.EmailField(max_length=254)
    password = models.TextField(max_length=16)
    Mobile = models.TextField(max_length=10)
    Plan = models.TextField(max_length=20)
    End_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.FirstName
