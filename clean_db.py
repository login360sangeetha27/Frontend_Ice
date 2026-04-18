import sqlite3
import os

# Path to the database
db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"  - {table[0]}")

# Delete all products from the correct table
cursor.execute('DELETE FROM products_product')

# Reset the sequence
cursor.execute('DELETE FROM sqlite_sequence WHERE name="products_product"')

# Commit the changes
conn.commit()
conn.close()

print('\n✅ All products deleted and ID sequence reset')
