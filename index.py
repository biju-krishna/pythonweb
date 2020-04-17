from flask import Flask, render_template, request

import datetime


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/more/<string:book_name>")
def more(book_name):
    return  render_template("more.html", book_name=book_name)

@app.route("/bookdetails/<string:book_name>")
def bookdetails(book_name):
    return render_template("bookdetails.html", book_name=book_name)

@app.route("/index")
def list():
    return render_template('index.html')

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method =='GET':
        return "Please submit the form instead"
    else:
        user_name=request.form.get("user_name")
        password=request.form.get("password")
        return render_template("index.html")