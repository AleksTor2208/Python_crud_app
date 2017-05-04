import os
from flask import Flask, flash, request, redirect, render_template, url_for

from model.product import Product

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/products", methods=["GET", "POST"])
def index():
    """ show list of products on the page """
    products = Product.get_all()   
    return render_template("index.html", products=products)

@app.route("/", methods=["GET", "POST"])
def redir_index():
    return redirect(url_for("index"))

@app.route("/product/new", methods=["GET", "POST"])
def add_product():
    """ Receive information from the user about new product
        call methods in product in order to add new product to database """
    if request.method == "GET":
        return render_template("add.html")
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["describtion"]
        price = request.form["price"]
        is_valid = validation(name, description, price)
        if is_valid:
            product = Product("", name, description, price)
            product.add_product()
            return redirect(url_for("index"))
        return render_template("add.html")

def validation(name, description, price):
    """ validate data the user has entered.
        Return True only in case all data is valid """
    if name == "":
        flash('Name is empty')
        return False
    if description == "":
        flash('Description is empty')
        return False
    if price == "":
        flash('Price is empty')
        return False
    if not price.isdigit():
        flash('Price should contain integers')
        return False
    if price.isdigit():
        price = int(price)
        if price < 0:
            flash('Price can not be less then 0')
            return False    
    return True

@app.route("/remove/<product_id>", methods=["GET", "POST"])
def remove_product(product_id):
    """ remove product from the list of products """
    my_product = Product.get_by_id(product_id)
    if my_product:
        my_product.remove_product()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)