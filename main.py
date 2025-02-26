from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from chettles import login_app  # Import the blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chess_inventory.db"
db = SQLAlchemy(app)

# Import models after initializing `db`
from inventory import Inventory  

# Register Blueprint
app.register_blueprint(login_app)

if __name__ == "__main__":
    app.run(debug=True)
