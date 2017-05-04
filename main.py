import os
from flask import Flask, flash, request, redirect, render_template, url_for

from model.product import product

app = Flask(__name__)
app.secret_key = "secret_key"


@app.route("/", methods=["GET", "POST"])
def index():
    
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)