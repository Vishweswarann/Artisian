import requests
from flask import Flask, render_template, request, url_for, flash, redirect, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import date, datetime
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "vanakam"
uploadFolder = "static/uploads"

app.secret_key = "vanakam"

os.makedirs(uploadFolder, exist_ok=True)
app.config['UPLOAD_FOLDER'] = uploadFolder




db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column("password", db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


# class Product(db.Model):
#     _id = db.Column("id", db.Integer, primary_key=True)
#     productCategory = db.Column("productCategory ", db.String(100))
#     productName = db.Column("productName", db.String(100))
#     productDescription = db.Column("productDescription", db.String(300))
#     productQuantity = db.Column("productQuantity", db.Integer)
#     productPrice = db.Column("productPrice",  db.Integer)
#     productAddress = db.Column("productAddress", db.String(100))
#     productPincode = db.Column("productPincode", db.Integer)
#
#     def __init__(self, productCategory, productName, productDescription,productQuantity, productPrice, productAddress, productPincode):
#         self.productCategory = productCategory
#         self.productName = productName
#         self.productDescription = productDescription
#         self.productQuantity = productQuantity
#         self.productPrice = productPrice
#         self.productAddress = productAddress
#         self.productPincode = productPincode
#

class pottery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,pro, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage
    
class weaving(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,prolength, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage
 

class carpentry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,pro, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage



class blacksmith(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage


class sculpture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage


class painting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer,)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage



class other(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    Name = db.Column(db.String(100))
    Description = db.Column(db.String(500))
    Quantity = db.Column(db.Integer)
    Price = db.Column(db.Integer)
    Width = db.Column(db.Integer)
    Height = db.Column(db.Integer)
    Length = db.Column(db.Integer)
    Address = db.Column(db.String(400))
    Contact = db.Column(db.Integer)
    Image = db.Column(db.String(100))

            # r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact)
    def __init__(self,userId, productName, productDescription,productQuantity, productPrice, productAddress,productHeight,productWidth,productLength, productContact, productImage):
        self.userId = userId
        self.Name = productName
        self.Description = productDescription
        self.Quantity = productQuantity
        self.Price = productPrice
        self.Address = productAddress
        self.Height = productHeight
        self.Width = productWidth
        self.Length = productLength
        self.Contact = productContact
        self.Image = productImage


@app.route("/")
@app.route("/home")
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
                session["userId"] = found_user.id
                print(session["userId"])
                return redirect(url_for('user'))
    
            else:
                # print("hello")
                flash("Invalid User credentials")
                return redirect(url_for('login'))
        else:
            print("hello")
            flash("Invalid User credentials")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route("/user", methods = ["POST", "GET"])
def user():
    potteryProducts = pottery.query.all()
    return render_template("user.html", potteryProducts = potteryProducts)

@app.route("/sell", methods = ["POST", "GET"])
def sell():
    if request.method == "POST":
        img = request.files["images"]
        category = request.form.get("category")
        proName = request.form.get("name")
        proDesription = request.form.get("description")
        proQuantity = request.form.get("quantity")
        proHeight = request.form.get("height")
        proWidth = request.form.get("width")
        proLength = request.form.get("length")
        proPrice = request.form.get("price")
        proAddress = request.form.get("address")
        proContact = request.form.get("phoneNumber")



        # gets the extension of the image file and stores it in ext
        ext = os.path.splitext(img.filename)[1]

        # creates a new filename with the name as date and time 

        new_imgname = f"{category}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"
        safe_imgname = secure_filename(new_imgname)

        img_path = app.config["UPLOAD_FOLDER"] + '/' + safe_imgname
        img.save(img_path)

        print(img_path)



        print(category)

        if category == "pottery":
            r = pottery(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "weaving":
            r = weaving(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "carpenrtry":
            r = carpentry(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "blacksmith":
            r = blacksmith(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "sculpture":
            r = sculpture(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "painting":
            r = painting(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        elif category == "other":
            r = other(session["userId"], proName, proDesription, proQuantity, proPrice, proAddress,proHeight, proWidth,proLength, proContact,img_path)

        else:
            return redirect(url_for('sell'))
        

        db.session.add(r)
        db.session.commit()
        flash("succesfully added")
        print("succesfully added")
        return redirect(url_for('sell'))


        
    return render_template("productSell.html")




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
    app.run(host="0.0.0.0", port=5000)
    # with app.app_context():  # Ensure db.create_all() runs in the app context
    #     db.create_all()
    # app.run(debug=True)
