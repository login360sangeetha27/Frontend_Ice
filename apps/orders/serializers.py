from rest_framework import serializers
from .models import Order
from apps.users.serializers import UserSerializer

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.JSONField(read_only=True)
    payment_info = serializers.JSONField(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'customer_name',
            'customer_email',
            'customer_phone',
            'shipping_address',
            'shipping_city',
            'shipping_state',
            'shipping_zip_code',
            'items',
            'payment_info',
            'total_price',
            'status',
            'created_at'
        ]
