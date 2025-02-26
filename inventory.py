from flask import Flask, request, jsonify
from login import users  # Import users to link inventory to accounts

app = Flask(__name__)

# Default inventory structure
default_inventory = {
    "shares": 100,  # Default currency amount
    "pieces": {
        "pawn": 8,
        "knight": 2,
        "bishop": 2,
        "rook": 2,
        "queen": 1,
        "king": 1
    },
    "packs": [],
    "cards": []
}

# Store inventories for users
inventories = {user: default_inventory.copy() for user in users}

@app.route('/inventory/<username>', methods=['GET'])
def get_inventory(username):
    if username in inventories:
        return jsonify({"username": username, "inventory": inventories[username]})
    return jsonify({"error": "User not found"}), 404

@app.route('/inventory/update', methods=['POST'])
def update_inventory():
    data = request.json
    username = data.get("username")
    updates = data.get("updates")

    if username not in inventories:
        return jsonify({"error": "User not found"}), 404

    # Apply updates (expects updates in {"shares": X, "pieces": {...}, "packs": [...], "cards": [...]})
    for key, value in updates.items():
        if key in inventories[username]:
            if isinstance(value, dict):  # If updating nested items like pieces
                inventories[username][key].update(value)
            else:
                inventories[username][key] = value

    return jsonify({"success": True, "inventory": inventories[username]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)  # Run inventory on a separate port