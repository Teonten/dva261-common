"""
Initialize and configure the Flask application.

This function creates a Flask application instance, loads configuration
settings from the config module, and registers the control routes blueprint.

Returns:
    Flask: A configured Flask application instance ready to be run.
"""
from flask import Flask
from config.settings import HOST, PORT

app = Flask(__name__)

# Load configurations
app.config["HOST"] = HOST
app.config["PORT"] = PORT

# Import and register routes
from app.routes import ctrl_routes
app.register_blueprint(ctrl_routes)