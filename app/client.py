#!/usr/local/DVA261/common-dva261/
from flask import jsonify, request
from pathlib import Path
from app.auth import authenticate_ctrl
from app.utils import log_message
from config.settings import NODE_CONF, NODE_STATUS, COM_INT
import logging
import time
import threading
import requests
import uuid
from config.settings import NODE_STATUS, COM_INT

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Send heartbeat
def heartbeat():
    """
    Time triggered heartbeat.
    Ctrl updates time delta for synchronization every heartbeat.
    """
    communicate(action='heartbeat')


# Threaded actuation command
def threaded_communicate(action, retries=COM_INT['max_retries']):
    """Threaded actuation command with retry logic."""
    hostname = NODE_CONF['hostname']
    host = '10.132.136.73' #NODE_CONF['ctrl_host']
    retries = retries
    endpoint = action
    action_id = str(uuid.uuid4())
    url = f"https://{host}/v1/nodes/{hostname}/{endpoint}"
    auth = {"Authorization": f"Bearer key_{hostname}"}
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    data = [NODE_STATUS]

    try:
        response = requests.post(url=url, json=data, auth=auth, headers=headers, verify=False, timeout=1)
        if response.status_code == 201:
            log_message(f"Command {action_id} sent to {hostname}: {action}")
            json_data = response.json()
            print(json_data)

            return data

    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        log_message(f"ERROR: {e} {action_id} to {hostname}. Retrying...")
        retries -= 1
        if retries > 0:
            threaded_communicate(endpoint, retries)

def communicate(action):
    hostname = NODE_CONF['hostname']
    endpoint = action
    data = [NODE_STATUS]
    """Send communication in a separate thread."""
    thread = threading.Thread(target=threaded_communicate, args=(hostname, endpoint,)
    )
    thread.daemon = True
    thread.start()

heartbeat()