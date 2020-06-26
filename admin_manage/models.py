from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    image = models.FileField(upload_to='uploads')
    stock = models.IntegerField()

    def __str__(self):
        return self.name