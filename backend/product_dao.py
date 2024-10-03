import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='root', database='grocery_store')

  return __cnx


def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product.get('name'), product.get('uom_id'), product.get('price_per_unit'))

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id== %s" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))
    #print(insert_new_product(connection,(
     #   'name': 'Apple',  # Ensure this field has a valid value
     #   'uom_id': 1,
      #  'price_per_unit': 10.5
    #))
