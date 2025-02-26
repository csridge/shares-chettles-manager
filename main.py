from flask import Flask, render_template
from flask_cors import CORS
from chettles import login_app  # Import the blueprint

app = Flask(__name__)
CORS(app)

app.register_blueprint(login_app)  # Register the login blueprint

@app.route('/')
def home():
    return render_template("login.html")  # Serve login page

if __name__ == "__main__":
    app.run(debug=True)
