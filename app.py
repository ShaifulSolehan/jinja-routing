from flask import Flask, render_template

app=Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")