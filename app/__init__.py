"""
Initialize and configure the Flask application.

This function creates a Flask application instance, loads configuration
settings from the config module, and registers the control routes blueprint.

Returns:
    Flask: A configured Flask application instance ready to be run.
"""
from flask import Flask
from config.settings import NODE_CONF

app = Flask(__name__)

# Load configurations
app.config['CTRL_HOST'] = NODE_CONF['ctrl_host']
app.config["HOST_IP"] = NODE_CONF['host_ip']
app.config["CTRL_PORT"] = NODE_CONF['ctrl_port']
app.config["HOSTNAME"] = NODE_CONF['hostname']

# Import and register routes
from app.routes import routes
app.register_blueprint(routes)