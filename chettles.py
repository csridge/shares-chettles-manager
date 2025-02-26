from flask import jsonify
import os
import threading

from login import login_app  # Import the login blueprint separately

def update_inventory():
    from main import db  # ✅ Lazy import to avoid circular import
    db.session.commit()
    return jsonify({"message": "Inventory updated"})

@app.route("/")
def home():
    return "Welcome to shares chettles manager. One note: this website is using shares as the currency."

def run_login():
    login_app.run(host="0.0.0.0", port=5000)

threading.Thread(target=run_login, daemon=True).start()

port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    from main import app  # ✅ Lazy import
    app.run(host="0.0.0.0", port=port)
