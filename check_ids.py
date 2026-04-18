import sqlite3
import os

# Path to the database
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all products
cursor.execute('SELECT id, name FROM products_product ORDER BY id')
products = cursor.fetchall()

print("Current Product IDs:")
for product_id, name in products:
    print(f"  ID {product_id}: {name}")

conn.close()
