from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.FloatField()
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='properties/')
    
    def __str__(self):
        return self.title

class UserPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_price_min = models.DecimalField(max_digits=10, decimal_places=2)
    preferred_price_max = models.DecimalField(max_digits=10, decimal_places=2)
    preferred_bedrooms = models.IntegerField()
    preferred_bathrooms = models.IntegerField()
    
    def __str__(self):
        return f"{self.user.username}'s preferences"