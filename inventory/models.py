from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add this line

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    barcode = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)    # Add this line
    updated_at = models.DateTimeField(auto_now=True)       # Add this line

    def __str__(self):
        return f"{self.name} (${self.price})"