from flask import Flask 
app=Flask(__name__)
@app.route("/<name>")
def home(name):
    return f"name is {name}"