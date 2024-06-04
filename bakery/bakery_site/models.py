from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)  
    content = models.TextField()              

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.PositiveIntegerField()  

    def __str__(self):
        return self.name
