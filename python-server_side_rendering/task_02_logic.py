from flask import Flask, render_template
import json

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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
