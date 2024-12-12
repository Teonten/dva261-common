from flask import Blueprint, jsonify, request
from app.auth import authenticate_node
from app.utils import log_message
from config.settings import NODE_STATUS, COM_INT, NODE_CONF
from app import actuators
import logging


# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Create a Flask Blueprint
routes = Blueprint("routes", __name__)

# Endpoints
@routes.route("/")
def index():
    """API status check.""" # HOSTNAME FOR NODE
    return jsonify({"message": f"{NODE_CONF['hostname']} API Server is running."}), 200

@routes.route(f"/v1/state", methods=["POST"])
@authenticate_node
def post_command():
    """Actuator command from ctrl."""
    pass
 
@routes.route("/status", methods=["GET"])
def system_status_view():
    """Fetch the current system status."""
    return jsonify(NODE_STATUS), 200