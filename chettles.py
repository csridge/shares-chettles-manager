from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

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
    return "Chess inventory is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
