from django.db import models


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    actors = models.CharField(max_length=100, blank=True, null=True)
    duration = models.IntegerField(max_length=100,null='True')
    created = models.DateTimeField(auto_now_add=True)
    video = models.FileField(upload_to='movies/')
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.title


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('Basic', 'Basic'),
        ('Standard', 'Standard'),
        ('Premium', 'Premium'),
    ]

    plan = models.CharField(max_length=15, choices=PLAN_CHOICES, null='True')
    rate = models.DecimalField(max_digits=10, decimal_places=2, null='True')
    duration_months = models.IntegerField(null='True')

    def __str__(self):
        return self.plan


class Customer(models.Model):
    FirstName = models.CharField(max_length=100, null='True')
    LastName = models.CharField(max_length=100,null='True')
    Email = models.EmailField(max_length=254,null='True')
    password = models.CharField(max_length=16,null='True')
    Mobile = models.CharField(max_length=10,null='True')
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE,null='True')
    End_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.FirstName
