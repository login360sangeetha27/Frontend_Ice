from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.CharField(max_length=512, blank=True, null=True)
    shipping_city = models.CharField(max_length=255, blank=True, null=True)
    shipping_state = models.CharField(max_length=255, blank=True, null=True)
    shipping_zip_code = models.CharField(max_length=30, blank=True, null=True)
    items = models.JSONField(blank=True, null=True, default=list)
    payment_info = models.JSONField(blank=True, null=True, default=dict)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_summary'

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
