from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institutions(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    types = [
        ('fundacja', 'fundacja'),
        ('organizacja pozarządowa', 'organizacja pozarządowa'),
        ('zbiórka lokalna', 'zbiórka lokalna')
        ]
    type = models.CharField(
        max_length=64,
        choices= types,
        default= 'fundacja'
    )
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institutions, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateTimeField()
    pick_up_time = models.DateTimeField()
    pick_up_comment = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')