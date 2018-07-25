from flask import Flask, render_template, request, redirect, url_for, flash
from wtforms import Form, StringField, IntegerField, validators
import sqlite3

app = Flask(__name__)
TABLE_NAME = "restaurant"
MENU_ID = "menu_id"
MENU_NAME = "menu_name"
MENU_PRICE = "menu_price"
MENU_QUANTITY = "menu_quantity"

connection = sqlite3.connect("database/restaurant.db")

connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + MENU_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   MENU_NAME + " TEXT, " + MENU_PRICE + " INTEGER, " +
                   MENU_QUANTITY + " INTEGER );")

class AddNewMenu(Form):
    menuName = StringField("Enter name of the menu item",
                           validators = [validators.DataRequired()])
    menuPrice = IntegerField("Enter price of the menu item",
                             validators = [validators.DataRequired()])
    menuQuantity = IntegerField("Enter the quantity of menu items",
                                validators = [validators.DataRequired()])

@app.route('/', methods = ["GET", "POST"])
def index():
    # return "Welcome to python."
    form = AddNewMenu(request.form)
    # and form.validate()
    if request.method == "POST":

        if form.validate():
            return redirect(url_for("newMenuItem"), code=302)
        else:
            flash("All fields are required.")
            return render_template("index.html", form = form)

    return render_template('index.html', form = form)

@app.route("/newMenuItem/", methods = ["GET", "POST"])
def newMenuItem():
    global connection
    global TABLE_NAME, MENU_NAME, MENU_PRICE, MENU_QUANTITY
    menuName = request.form["menuName"]
    menuPrice = request.form["menuPrice"]
    menuQuantity = request.form["menuQuantity"]
    menuItem = {
        'name': menuName,
        'price': menuPrice,
        'quantity': menuQuantity
    }

    connection = sqlite3.connect("database/restaurant.db")
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + MENU_NAME + ", " + MENU_PRICE + ", " + MENU_QUANTITY +
                       " ) VALUES ( '" + menuName + "', " + menuPrice +", " + menuQuantity + " );")
    print("values inserted.")
    connection.commit()

    return render_template("AddNewMenuItem.html", menuItem = menuItem)

@app.route("/listMenu")
def listMenu():
    connection = sqlite3.connect("database/restaurant.db")
    kunal = connection.execute("SELECT * FROM " + TABLE_NAME)
    # print(cursor)
    # for row in cursor:
    #     print("ID is: ", row[0])
    #     print("Name is: ", row[1])
    #     print("Price is: ", row[2])
    #     print("Quantity is: ", row[3])

    rows = kunal.fetchall()

    # return "Print the list of menu's from the database."
    return render_template("DisplayMenuItems.html", rows = rows)


@app.route('/hello/<string:username>/')
def helloUsername(username):
    return render_template('hello.html', name = username)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page-not-found.html"),404

if __name__ == "__main__":
    app.run()
    app.register_error_handler(404, pageNotFound)