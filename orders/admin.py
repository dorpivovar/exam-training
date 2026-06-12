from django.contrib import admin
from .models import Orders

# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'quanity', 'order_date', 'status', 'created_at')
    list_filter = ('status', )
    search_fields = ('customer_name', 'product_name')

    