from flask import Blueprint, jsonify, request
from app.auth import authenticate_node
from app.utils import log_message
from config.settings import ACK_TIMEOUT, MAX_RETRIES
from config.settings import CTRL_HOST, HOSTNAME, NODE_STATUS, COM_INT
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
    return jsonify({"message": f"{HOSTNAME} API Server is running."}), 200

@routes.route(f"/v1/state", methods=["POST"])
@authenticate_node
def post_command():
    """Actuator command from ctrl."""
    try:
        data = request.json

        if NODE_STATUS["time_delta"] is None:
            # Assign time delta during the first heartbeat
            NODE_STATUS["time_delta"] = COM_INT['time_delta']
            log_message(f"Assigned time delta {NODE_STATUS['time_delta']} to {HOSTNAME}.")

            # Update the heartbeat timestamp
            NODE_STATUS["heartbeat"] = node_time
            log_message(f"Heartbeat updated for node {HOSTNAME} at {node_time}.")

            return jsonify(NODE_STATUS), 200
        else:
            return jsonify({"message": "Node not found"}), 404
    except Exception as e:
        logging.error(f"Error in /heartbeat: {e}")
        return jsonify({"message": "Bad Request"}), 400

    return jsonify(NODE_STATUS), 200

@routes.route("/status", methods=["GET"])
def system_status_view():
    """Fetch the current system status."""
    return jsonify(NODE_STATUS), 200