from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    made_in = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f'{self.name} {self.made_in} {self.category} {self.price}'

    class Meta:
        verbose_name = 'Product'