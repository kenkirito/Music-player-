from flask import Flask, render_template, request, redirect
from mysql.connector import connect
import random
import string
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run()