#Import SQL
import mysql.connector

#Create Database Class
class Database:
    
    #Create 'Database' Class constructor with arguments for accessing 'supre_db' Database
    def __init__(self, host, user, password, database):
         
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        #Check user account values and connects to 'supre_db' Database if correct
        self.db = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
        )
        
        #Instantiate cursor for SQL statements
        self.cursor = self.db.cursor()
    
    #Add Product Data to 'products' Table
    def add_product(self, name, stocks, price):
        self.sql = f"INSERT INTO products (name, stocks, price) VALUES ('{name}','{stocks}','{price}')"
        self.cursor.execute(self.sql)
        self.db.commit()
    
    #Update Product Data from 'products' Table
    def update_product(self, id, name, stocks, price):
        self.sql = f"UPDATE products SET name = '{name}', stocks = '{stocks}', price = '{price}' WHERE id = {id}"
        self.cursor.execute(self.sql)
        self.db.commit()


    #Delete Product Data from 'products' Table
    def remove_product(self, id):
        self.sql = f"DELETE FROM products WHERE id = {id}"
        self.cursor.execute(self.sql)
        self.db.commit()



