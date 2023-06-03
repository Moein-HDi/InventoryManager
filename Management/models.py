from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Inventory(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.city

class InventoryProduct(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    Inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

from accounts.models import CustomUser
    
class Order(models.Model):
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(InventoryProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str ('{name} ({prod} * {quan})'.format(name=self.username.username, prod=self.product, quan=self.quantity))
        


