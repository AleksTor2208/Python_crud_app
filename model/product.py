from sql_connect import SQL

class Product:
    """ product class, which represents each product described in database. """
    def __init__(self, id, name, description, price):
        """ class constructor"""
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def get_all():
        """ retreive all data from the database. Return list of product instances. """
        product_list = []
        query = "SELECT * FROM products;"
        products = SQL.execute_query(query)
        if products is None:
            return False
        for row in products:
            product = Product(row[0], row[1], row[2], row[3])
            product_list.append(product)
        return product_list

    def add_product(self):
        """ send query and parameters to sql execution method 
            in order to add new product to database. """
        query = "INSERT INTO products (name, description, price) VALUES(?, ?, ?);"
        params = [self.name, self.description, self.price]
        SQL.execute_query(query, params)

    @staticmethod
    def get_by_id(product_id):
        """ get product by it's id number. """
        products = Product.get_all()
        for product in products:
            if product.id == int(product_id):
                return product
        return False

    def remove_product(self):
        """ send query and parameters to sql execution method 
            in order to remove the product from database. """
        query = "DELETE FROM products WHERE ID=?;"
        params = [self.id]
        SQL.execute_query(query, params)
