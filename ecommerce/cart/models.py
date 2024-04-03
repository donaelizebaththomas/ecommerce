from django.db import models
from shop.models import product
from django.contrib.auth.models import User

# Create your models here.


class Cart(models.Model):
    Product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        """ to print the subtotal of each product self is i, i is the current product """
        return self.quantity * self.Product.price

    def __str__(self):
        """ to print the product name instead of displaying object """
        return self.Product.name

class Order(models.Model):
    address=models.TextField()
    phone=models.BigIntegerField()
    Product = models.ForeignKey (product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    no_of_item=models.IntegerField()
    ordered_date=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(max_length=30,default="pending")
    delivery_status=models.CharField(max_length=30,default="pending")

    def __str__(self):
        return self.user.username

class Account(models.Model):
    acctype=models.CharField(max_length=20)
    acctnum=models.BigIntegerField()
    amount=models.IntegerField()

    def __str__(self):
        return str(self.acctnum)