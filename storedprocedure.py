import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="inventory"
)

cursor = conn.cursor()

# Call the stored procedure
product_name = 'Laptop'
quantity = 5

cursor.callproc('add_product', [product_name, quantity])

# Commit the transaction
conn.commit()

# Check results (optional)
cursor.execute("SELECT * FROM inventory")
for row in cursor.fetchall():
    print(row)

# Cleanup
cursor.close()
conn.close()
