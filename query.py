from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

all = Users.query.all()

for user in all:
    print(f"ID: {user._id}, Name: {user.name}, Email: {user.email}, Password: {user.password}")


if __name__ == "__main__":
    with app.app_context():  # Ensure db.create_all() runs in the app context
        db.create_all()
    app.run(debug=True)
