from django.db import models
from admin_manage.models import Product

# Create your models here.
class Order_Item(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField() 

class Order(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    status = models.CharField(max_length=30, default=None)
    total = models.IntegerField(default=0)
    order_list = models.ManyToManyField(Order_Item)

    def __str__(self):
        return self.firstname + self.lastname
