from flask import Flask, request, jsonify, render_template
import hashlib
from flask_cors import CORS
from inventory import default_inventory

app = Flask(__name__)
CORS(app)

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

@app.route('/')
def home():
    return render_template("login.html")  # Serve login page

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in users and users[username]["password"] == hashlib.sha256(password.encode()).hexdigest():
        return jsonify({"success": True, "inventory_url": f"https://shares-chettles-manager.onrender.com/inventory/{username}"})
    
    return jsonify({"success": False, "message": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
