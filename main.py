from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class sellerUsers(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/seller_signup", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form.get("name") 
        email = request.form.get("email") 
        password = request.form.get("password") 

        addUser = sellerUsers(name, email, password)
        db.session.add(addUser)
        db.session.commit()

    return render_template("signup.html")

@app.route("/seller_login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email") 
        password = request.form.get("password") 


        found_user = sellerUsers.query.filter_by(email = email).first()
        if found_user:
            if found_user.password == password:
                return render_template("user.html")
    
    return render_template("login.html")




if __name__ == "__main__":
    with app.app_context():  # Ensure db.create_all() runs in the app context
        db.create_all()
    app.run(debug=True)
