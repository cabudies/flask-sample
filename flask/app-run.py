from flask import Flask, render_template
# import flask

app = Flask(__name__)

@app.route('/')
def index():
    # return "Welcome to python."
    return render_template('index.html')

@app.route('/hello')
def helloWorld():
    return "Hello World. This is an return value."

@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page-not-found.html"),404

if __name__ == "__main__":
    app.run()
    app.register_error_handler(404, pageNotFound)