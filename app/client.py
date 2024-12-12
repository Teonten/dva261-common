#!/usr/local/DVA261/common-dva261/
from flask import jsonify, request
from pathlib import Path
from app.utils import log_message
from config.settings import NODE_CONF, NODE_STATUS, COM_INT
from config.tls_config import get_tls_context
import logging
import requests
import uuid
import json
from urllib3 import disable_warnings
from config.settings import NODE_STATUS, COM_INT
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)
# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Send heartbeat
def heartbeat():
    """
    Time triggered heartbeat.
    Ctrl updates time delta for synchronization every heartbeat.
    """
    print('sending heartbeat')
    communicate(action='heartbeat')

def communicate(action):
    """Threaded actuation command with retry logic."""
    hostname = NODE_CONF['hostname']
    host = NODE_CONF['ctrl_host']
    retries = COM_INT['max_retries']
    endpoint = action
    ca = get_tls_context().get_ca_certs()
    api_key = NODE_CONF['api_key']
    action_id = str(uuid.uuid4())
    url = f"https://{host}/v1/nodes/{hostname}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    # NODE_STATUS should already be a dictionary; no need to JSON-encode it
    data = NODE_STATUS
    logging.debug(f"Prepared data for request: {data}")

    try:
        response = requests.post(
            url=url,
            json=data,  # Send dictionary directly
            headers=headers,
            cert=ca,
            verify=False,
            timeout=1
        )
        logging.debug(f"Response status code: {response.status_code}")

        ack = None

        if response.status_code == 200:
            log_message(f"Command {action_id} sent to {hostname}: {action}")            
            var = response.json()
            print(var)
            ack = True

        elif response.status_code == 201:
            log_message(f"Command {action_id} sent to {hostname}: {action}")
            var = response.json()
            print(var)
            ack = True

        return ack

    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        log_message(f"ERROR: {e} {action_id} to {hostname}. Retrying...")