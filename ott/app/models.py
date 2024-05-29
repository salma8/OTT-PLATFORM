from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=100,blank=True, null=True)
    genre = models.CharField(max_length=100,blank=True, null=True)
    director = models.CharField(max_length=100,blank=True, null=True)
    actors = models.CharField(max_length=100,blank=True, null=True)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='static/movies')
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title

class Subscription(models.Model):
    PLAN_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    plan = models.CharField(max_length=15, choices=PLAN_CHOICES)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField()

    def __str__(self):
        return self.plan

class Customer(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)
    Mobile = models.CharField(max_length=10)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    End_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.FirstName
