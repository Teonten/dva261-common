from flask import request, jsonify
from functools import wraps
from config.settings import CTRL_KEY

def authenticate_node(f):
    """
    A decorator function that authenticates API requests using an API key.

    This function checks for the presence of a valid API key in the request headers.
    If the API key is missing or invalid, it returns an "Unauthorized" response.
    If the API key is valid, it allows the decorated function to be executed.

    Args:
        f (function): The function to be decorated.

    Returns:
        function: A wrapper function that performs the authentication check
                  before calling the decorated function.

    The wrapper function:
    - Extracts the API key from the "Authorization" header.
    - Validates the API key against the predefined API_KEYS.
    - Returns a 401 Unauthorized response if the API key is invalid or missing.
    - Calls the decorated function if the API key is valid.
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if api_key != CTRL_KEY:
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)
    return wrapper