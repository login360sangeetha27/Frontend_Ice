from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, get_products, get_product

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('products/', get_products, name='products-list'),
    path('products/<int:pk>/', get_product, name='product-detail'),
]

urlpatterns += router.urls
