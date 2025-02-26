# i love how this file is pne of the latest created file
from chettles import app as chettles_app
from login import app as login_app

# Merge both Flask apps
from flask import Flask
app = Flask(__name__)

app.register_blueprint(chettles_app)
app.register_blueprint(login_app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)