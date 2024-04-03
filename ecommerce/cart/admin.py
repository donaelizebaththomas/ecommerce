from django.contrib import admin
from cart.models import Cart,Order,Account


# Register your models here.


admin.site.register(Cart)
admin.site.register(Account)
admin.site.register(Order)

