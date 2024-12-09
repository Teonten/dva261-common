"""
Initialize and configure the Flask application.

This function creates a Flask application instance, loads configuration
settings from the config module, and registers the control routes blueprint.

Returns:
    Flask: A configured Flask application instance ready to be run.
"""
from flask import Flask
from config.settings import CTRL_HOST, HOST_IP, HOSTNAME, PORT

app = Flask(__name__)

# Load configurations
app.config['CTRL_HOST'] = CTRL_HOST
app.config["HOST_IP"] = HOST_IP
app.config["PORT"] = PORT
app.config["HOSTNAME"] = HOSTNAME

# Import and register routes
from app.routes import routes
app.register_blueprint(routes)