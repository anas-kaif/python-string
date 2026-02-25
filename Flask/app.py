from flask import Flask,request,session,Response,url_for,redirect
app=Flask(__name__)
app.secret_key="anaskaif"
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        Username=request.form.get("Username")
        Password=request.form.get("Password")
        if Username=="admin" and Password=="123":
            session["User"]=Username

            return redirect(url_for("Welcome"))
        else:
            return Response("In-valid Username or Password!",mimetype="text/plain")
    return '''
        <h2> Login page</h2>
        <form method="POST">
        Username:<input type="text" name="Username"><br>
        Password:<input type="password" name="Password"><br>
        <input type="submit" value="Login">
        </form>
    '''
@app.route("/Welcome")
def Welcome():
    if "User" in session:
        return f'''<h2>Welcome,{session["User"]}!</h2>
                <a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("User",None)
    return redirect(url_for("login"))