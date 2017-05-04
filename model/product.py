from sql_connect import SQL

class Product:
    """ product class, which represents each product described in database """
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    @staticmethod
    def get_all():
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
        query = "INSERT INTO products (name, description, price) VALUES(?, ?, ?);"
        params = [self.name, self.description, self.price]
        SQL.execute_query(query, params)
