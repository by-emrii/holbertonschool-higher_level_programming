from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/items")
def items():
    with open("items.json") as f:
        # load data from json file
        data = json.load(f)

    # get list of items and sends it to template as a variable called items
    item_list = data.get("items", [])

    return render_template("items.html", items=item_list)
    # look for 'items' key inside dict data and return value, if not exists, return empty list instead of crashing


@app.route("/products")
def products():
    # get query args from URL
    source_query = request.args.get("source")
    id_query = request.args.get("id")

    # load from json
    if source_query == "json":
        with open("products.json") as f:
            products = json.load(f)

    # load from csv
    elif source_query == "csv":
        with open("products.csv") as f:
            products = list(csv.DictReader(f))

    else:
        return render_template(
            "product_display.html", error="Wrong source", products=[]
        )

    # If ID was provided, filter products
    if id_query:
        filtered = [p for p in products if str(p["id"]) == str(id_query)]

        if not filtered:
            return render_template(
                "product_display.html", error="Product not found", products=[]
            )
        # only one product will match
        return render_template("product_display.html", products=filtered, error=None)
    # if no ID, show everything
    return render_template("product_display.html", products=products, error=None)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
