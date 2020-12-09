from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    model = models.CharField(max_length=300, default='none')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='products')
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name


class ProductInstance(models.Model):
    uuid = models.UUIDField()
    purchase_date = models.DateField(auto_now=False, auto_now_add=False)
    sold_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='instances')

    def __str__(self):
        return self.uiud
