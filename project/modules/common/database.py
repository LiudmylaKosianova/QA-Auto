import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("/home/carmin/Public/QA-Auto/project/become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        self.cursor.execute("SELECT sqlite_version();")
        message = self.cursor.fetchall()
        print(f"Successfully connected. SQLite version: {message}")

    def get_all_users(self):
        self.cursor.execute("SELECT name, address, city from customers")
        users = self.cursor.fetchall()
        return users
    
    def get_user_address_by_name(self, name):
        self.cursor.execute("SELECT address, city, postalCode, country FROM customers\
                             WHERE name = \"{name}\"")
        address = self.cursor.fetchall()
        return address
    
    def update_product_qt_by_id(self, id, qt):
        self.cursor.execute("UPDATE product SET quantity = {qt} WHERE id = {id}")
