from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import threading
import login
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chess_inventory.db"
db = SQLAlchemy(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.String(50), unique=True, nullable=False)
    inventory = db.Column(db.Text, nullable=False)  # JSON string

with app.app_context():
    db.create_all()

@app.route("/inventory/<player_id>", methods=["GET"])
def get_inventory(player_id):
    player = Inventory.query.filter_by(player_id=player_id).first()
    if player:
        return jsonify({"player_id": player.player_id, "inventory": eval(player.inventory)})
    return jsonify({"player_id": player_id, "inventory": []})

@app.route("/inventory/update", methods=["POST"])
def update_inventory():
    data = request.json
    player = Inventory.query.filter_by(player_id=data["player_id"]).first()
    
    if player:
        player.inventory = str(data["inventory"])
    else:
        new_player = Inventory(player_id=data["player_id"], inventory=str(data["inventory"]))
        db.session.add(new_player)

    db.session.commit()
    return jsonify({"message": "Inventory updated"})
@app.route("/")

def home():
    return "Welcome to shares chettles manager. One note: this website is using shares as the currency but shares chettles is not implemented into shares economy. Don't ask why it is using shares again"

def run_login():
    login.app.run(host="0.0.0.0", port=5000)

threading.Thread(target=run_login, daemon=True).start()

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
