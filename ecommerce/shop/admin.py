from django.contrib import admin
from django.http import HttpRespones
from shop.models import category,product

# Register your models here.


admin.site.register(category)
admin.site.register(product)