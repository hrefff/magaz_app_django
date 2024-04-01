from django.contrib import admin
from .models import Income, Sale, Inventory

# Register your models here.
admin.site.register(Income)
admin.site.register(Sale)
admin.site.register(Inventory)
