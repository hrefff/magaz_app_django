from django.db import models

class Group(models.Model):
    group_name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.group_name 


class Item(models.Model):
    item_name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group)
    
    def __str__(self):
        return self.item_name
