from flask import Flask, request, jsonify, render_template
import hashlib
from flask_cors import CORS
from inventory import default_inventory

app = Flask(__name__)
CORS(app)

# Example users
users = {
    "jsaidoru": {"password": hashlib.sha256("pyaidoru".encode()).hexdigest()},
    "availablegreen": {"password": hashlib.sha256("availablegreen".encode()).hexdigest()}
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
    app.run(host='0.0.0.0', port=5003)
