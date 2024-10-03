
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


if __name__ == '__main__':
    import datetime
    import mysql.connector

    __cnx = None


    def get_sql_connection():
        print("Opening mysql connection")
        global __cnx

        if __cnx is None:
            __cnx = mysql.connector.connect(user='root', password='root', database='grocery_store')

        return __cnx


    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(get_uoms(connection))