from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_urls = models.CharField(max_length=2845)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField()
    discount = models.FloatField()
