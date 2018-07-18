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

if __name__ == "__main__":
    app.run()