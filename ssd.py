from flask import Flask
from home import home  # Import the updated Blueprint

app = Flask(__name__)
app.register_blueprint(home)  # Register the Blueprint

# Note: No app.run() is needed for deployment
