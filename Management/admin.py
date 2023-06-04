from django.contrib import admin
from .models import *


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Inventory)
admin.site.register(InventoryProduct)
admin.site.register(Order)
