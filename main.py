from flask import Flask, render_template, request, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "vanakam"
uploadFolder = "static/uploads"

os.makedirs(uploadFolder, exist_ok=True)
app.config['UPLOAD_FOLDER'] = uploadFolder




db = SQLAlchemy(app)


class Users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Product(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    productCategory = db.Column("productCategory ", db.String(100))
    productName = db.Column("productName", db.String(100))
    productDescription = db.Column("productDescription", db.String(300))
    productQuantity = db.Column("productQuantity", db.Integer)
    productPrice = db.Column("productPrice",  db.Integer)
    productAddress = db.Column("productAddress", db.String(100))
    productPincode = db.Column("productPincode", db.Integer)

    def __init__(self, productCategory, productName, productDescription,productQuantity, productPrice, productAddress, productPincode):
        self.productCategory = productCategory
        self.productName = productName
        self.productDescription = productDescription
        self.productQuantity = productQuantity
        self.productPrice = productPrice
        self.productAddress = productAddress
        self.productPincode = productPincode
    


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/signup", methods = ["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form.get("name") 
        email = request.form.get("email") 
        password = request.form.get("password") 
        
        foundName = Users.query.filter_by(name = name).first()
        foundEmail = Users.query.filter_by(email = email).first()

        if foundName :
           flash("The user already exist") 
           return redirect(url_for('signup'))
        if foundEmail:
           flash("The email already exist") 
           return redirect(url_for('signup'))
            
        addUser = Users(name, email, password)
        db.session.add(addUser)
        db.session.commit()
        flash("Succesfully Added")
        return redirect(url_for('login'))

    return render_template("signup.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email") 
        password = request.form.get("password") 


        found_user = Users.query.filter_by(email = email).first()
        if found_user:
            if found_user.password == password:
                return redirect(url_for('user'))
    
            else:
                print("hello")
                flash("Invalid User credentials")
                return redirect(url_for('login'))
        else:
            print("hello")
            flash("Invalid User credentials")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/user", methods = ["POST", "GET"])
def user():
    return render_template("user.html")

@app.route("/add", methods = ["POST", "GET"])
def add():
    if request.method == "POST":
        file = request.files["images"]
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))
        category = request.form.get("category")
        proName = request.form.get("name")
        proDesription = request.form.get("description")
        proQuantity = request.form.get("quantity")
        proPrice = request.form.get("price")
        proAddress = request.form.get("address")
        proPincode = request.form.get("pincode")

        print(category)
        r = Product(category, proName, proDesription, proQuantity, proPrice, proAddress, proPincode)
        db.session.add(r)
        db.session.commit()
        flash("succesfully added")
        return redirect("url_for('add')")


        
    return render_template("productAdd.html")




# for admin purposes - fetching all the rows and deleting a particular row
@app.route("/query-all", methods = ["POST", "GET"])
def query_all():
    if request.method == "POST":
        row = request.form.get("row")
        user = Users.query.filter_by(name =row ).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            print("deleted")
    all = Users.query.all()
    if all:
        for user in all:
            print(f"ID: {user._id}, Name: {user.name}, Email: {user.email}, Password: {user.password}")
    
    return render_template("admin.html")
    
@app.route("/view", methods = ["POST", "GET"])
def view():
    return render_template("view.html")





if __name__ == "__main__":
    with app.app_context():  # Ensure db.create_all() runs in the app context
        db.create_all()
    app.run(debug=True)
