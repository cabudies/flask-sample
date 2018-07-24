from flask import Flask, render_template, request, redirect, url_for, g
from wtforms import Form, StringField, IntegerField, validators

app = Flask(__name__)


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
    if request.method == "POST" and form.validate():

        return redirect(url_for("newMenuItem"), code=302)

    return render_template('index.html', form = form)

@app.route("/newMenuItem/", methods = ["GET", "POST"])
def newMenuItem():
    menuName = request.form["menuName"]
    menuPrice = request.form["menuPrice"]
    menuQuantity = 100
    menuItem = {
        'name': menuName,
        'price': menuPrice,
        'quantity': menuQuantity
    }
    # return "New Menu Item Page."
    return render_template("AddNewMenuItem.html", menuItem = menuItem)


@app.route('/hello/<string:username>/')
def helloUsername(username):
    return render_template('hello.html', name = username)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page-not-found.html"),404

if __name__ == "__main__":
    app.run()
    app.register_error_handler(404, pageNotFound)