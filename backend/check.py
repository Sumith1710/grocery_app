import mysql.connector

connection = None  # Initialize connection variable

try:
    connection = mysql.connector.connect(
        user='root',
        password='root',
        database='grocery_store'
    )
    print("Connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection:
        connection.close()
