from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null = True)
    email = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door', 'Out Door')
    )
    name = models.CharField(max_length=64,null=True)
    price = models.FloatField(null= True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null =True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete =models.SET_NULL)
    date_created = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.product.name