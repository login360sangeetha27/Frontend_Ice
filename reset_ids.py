#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'icecream_project.settings')
django.setup()

from apps.products.models import Product
from django.db import connection

# Delete all products
Product.objects.all().delete()

# Reset the sequence
cursor = connection.cursor()
cursor.execute('DELETE FROM sqlite_sequence WHERE name="apps_products_product"')

print('All products deleted and ID sequence reset to start from 1')
