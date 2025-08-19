from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'barcode', 'category', 'price', 'stock_quantity', 'is_low_stock')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'barcode')
    list_editable = ('price', 'stock_quantity')
    
    def is_low_stock(self, obj):
        return obj.stock_quantity < 10   # threshold value (e.g., 10)
    is_low_stock.boolean = True
    is_low_stock.short_description = "Low Stock"