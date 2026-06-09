from django.contrib import admin
from .models import Product


# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock', 'sku', 'created_at')
    list_filter = ('category', )
    search_fields = ('name', 'sku')
        