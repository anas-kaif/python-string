from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Kaif, Flask is running!"

app.run(debug=True)
