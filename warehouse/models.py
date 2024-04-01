from django.db import models
from item.models import Item

# Create your models here.

# Income
class Income(models.Model):
    income_order = models.CharField(max_length=50, unique=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.income_order


# Inventory
class Inventory(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.item_id.item_name   


# Sale
class Sale(models.Model):
    sale_order = models.CharField(max_length=50, unique=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sale_order


# Report
class Report(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

