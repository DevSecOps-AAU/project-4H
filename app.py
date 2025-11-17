from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from src.users.services import UserServices


app =Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def login():
    return render_template("login.html")


@app.route('/login-process', methods=['POST'])
def login_process():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        row = UserServices.login(username, password)
        if not row:
            return redirect(url_for("login"))
        return redirect(url_for("home"))
    


@app.route('/register')
def register():
    return render_template("register.html")



@app.route('/register-process', methods=['POST'])
def register_process():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        # confirm_password = request.form.get('confirm_password')
        row = UserServices.register(username, email, password)
        if not row:
            return redirect(url_for("register"))
        return redirect(url_for("login"))
    
    

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html")


@app.route('/search', methods=['GET'])
def search_places():
    query = request.args.get('query')          
    features = request.args.get('features')    

    
    return render_template("home.html", username=session['username'])  




if __name__ == "__main__":
    app.run(debug=True)