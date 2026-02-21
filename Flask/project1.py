from flask import Flask
app=Flask(__name__)
@app.route('/')
def greet():
    return "hello anas"
@app.route("/home")
def hoem():
    return "This is my Flask first home page"
if __name__=="__main__":
    app.run(debug=True)