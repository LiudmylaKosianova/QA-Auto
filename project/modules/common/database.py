import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("/home/carmin/Public/learning-QA-Auto/project/become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        message = self.cursor.fetchall()
        print(f"Successfully connected. SQLite version: {message}")

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city FROM customers")
        users = self.cursor.fetchall()
        return users
    
    def get_user_address_by_name(self, name):
        self.cursor.execute(f"SELECT address, city, postalCode, country\
                              FROM customers\
                              WHERE name = \"{name}\"")
        address = self.cursor.fetchall()
        return address
    
    def update_product_qt_by_id(self, id, qt):
        self.cursor.execute(f"UPDATE products SET quantity = {qt} WHERE id = {id}")
        self.connection.commit()

    def select_product_qt_by_id(self, id):
        self.cursor.execute(f"SELECT quantity FROM products WHERE id = {id}")
        qt = self.cursor.fetchall()
        return qt
    
    def select_product_attr_by_id(self, id):
        self.cursor.execute(f"SELECT name, description, quantity FROM products WHERE id = {id}")
        qt = self.cursor.fetchall()
        return qt
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
                  VALUES ({product_id}, \"{name}\", \"{description}\", {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, id):
        self.cursor.execute(f"DELETE FROM products WHERE id = {id}")
        self.connection.commit()

    def get_detailed_order(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        info = self.cursor.fetchall()
        return info
    
    
