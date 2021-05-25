from django.contrib import admin
from eshop.models import *
# Register your models here.
class ShopAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ShopAdmin)