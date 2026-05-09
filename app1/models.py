from django.db import models

# Create your models here.
class Products(models.Model):
    size_choice =[
        ('Extra Small', 'XS'),
        ('Small', 'S'),
        ('Medium', 'M'),
    ]

    colors_choice = [
        ('White', 'W'),
        ('Black', 'B'),
        ('Red', 'R'),
        ('Blue', 'B'),
        ('Yellow', 'Y'),
    ]

    product_name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    size = models.CharField(choices=size_choice, default='M')
    colors = models.CharField(choices=colors_choice, default='Black')



    def __str__(self):
        return f"{self.product_name} - ${self.price}"
    
