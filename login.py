from flask import Flask, request, jsonify
import hashlib
from inventory import default_inventory

app = Flask(__name__)

# Example user database (move to a file or DB in the future)
users = {
    "jsaidoru": {"password": hashlib.sha256("pyaidoru".encode()).hexdigest()},
    "availablegreen": {"password": hashlib.sha256("availablegreen".encode()).hexdigest()},
    "bozo0069": {"password": hashlib.sha256("gothamchesssucks".encode()).hexdigest()},
    "erix_senpai": {"password": hashlib.sha256("ihategenshin".encode()).hexdigest()},
    "kan1234567891011121314": {"password": hashlib.sha256("kanlol".encode()).hexdigest()},
    "ghoda": {"password": hashlib.sha256("bulletenjoyer".encode()).hexdigest()},
    ".wigeon.": {"password": hashlib.sha256("kyobir".encode()).hexdigest()},
    "i_am_not_kk": {"password": hashlib.sha256("iamkk".encode()).hexdigest()},
    "stedwesd": {"password": hashlib.sha256("car95".encode()).hexdigest()}
}

# Store user inventories (temporary, should use a database)
user_inventories = {}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    # Check if user exists and password matches
    if username in users and users[username]["password"] == hashlib.sha256(password.encode()).hexdigest():
        # Assign default inventory if user logs in for the first time
        if username not in user_inventories:
            user_inventories[username] = default_inventory.copy()
        
        return jsonify({
            "success": True,
            "inventory_url": f"https://shares-chettles-manager.onrender.com/inventory/{username}"
        })
    
    return jsonify({"success": False, "message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
