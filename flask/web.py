from flask import Flask, render_template

#creat a Flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

def index():
    return '<h1> hello world </h1>'