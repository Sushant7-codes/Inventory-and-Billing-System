from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product

class Sale(models.Model):  # Changed from "Sales" to "Sale"
    PAYMENT_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('wallet', 'Digital Wallet'),
    ]
    
    STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Cashier
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_CHOICES)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='paid')
    
    def __str__(self):
        return f"Sale #{self.id} - ${self.total_amount}"

class SaleItem(models.Model):  # Changed from "SalesItem" 
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of sale
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.quantity}x {self.product.name}"