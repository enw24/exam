from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')
    name = models.CharField(blank=True, max_length=100)
    brand = models.CharField(blank=True, max_length=100)
    url = models.URLField(max_length=2000, default="espn.com")

class Clothes(models.Model):
    size = models.CharField(blank=True, max_length=3)
    info = models.ForeignKey(Product, on_delete=models.CASCADE)

class Jewelery(models.Model):
    extrainfo = models.CharField(blank=True, max_length=100)
    info = models.ForeignKey(Product, on_delete=models.CASCADE)

class Vehicle(models.Model):
    color = models.CharField(blank=True, max_length=100)
    info = models.ForeignKey(Product, on_delete=models.CASCADE)

class Pet(models.Model):
    animal = models.CharField(blank=True, max_length=100)
    info = models.ForeignKey(Product, on_delete=models.CASCADE)

class Other(models.Model):
    info = models.ForeignKey(Product, on_delete=models.CASCADE)

