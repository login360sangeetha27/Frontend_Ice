from decimal import Decimal
from django.db.models import Q
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer


@csrf_exempt
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def orders_view(request):
    user = request.user
    if request.method == 'GET':
        orders = Order.objects.filter(
            Q(user=user) | Q(customer_email__iexact=user.email)
        ).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        items = request.data.get('items')
        total_price = request.data.get('total_price')

        if items:
            order_items = []
            for item in items:
                order_items.append({
                    'product_id': item.get('product_id') or item.get('id'),
                    'product_name': item.get('product_name') or item.get('name'),
                    'quantity': item.get('quantity', 1),
                    'price': item.get('price', 0)
                })
            if not total_price:
                total_price = sum(
                    Decimal(str(item.get('price', 0))) * int(item.get('quantity', 1))
                    for item in order_items
                )
        else:
            return Response({'error': 'Order items are required'}, status=status.HTTP_400_BAD_REQUEST)

        customer_info = request.data.get('customerInfo', {})
        customer_email = customer_info.get('email', '')
        if customer_email:
            customer_email = customer_email.strip().lower()
        order = Order.objects.create(
            user=user,
            customer_name=customer_info.get('cardName') or customer_info.get('name'),
            customer_email=customer_email,
            customer_phone=customer_info.get('phone'),
            shipping_address=customer_info.get('address'),
            shipping_city=customer_info.get('city'),
            shipping_state=customer_info.get('state'),
            shipping_zip_code=customer_info.get('zipCode'),
            items=order_items,
            payment_info=customer_info,
            total_price=Decimal(str(total_price))
        )

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
