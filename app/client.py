#!/usr/local/DVA261/common-dva261/
from flask import jsonify, request
from pathlib import Path
from app.utils import log_message
from config.settings import NODE_CONF, NODE_STATUS, COM_INT
from config.tls_config import get_tls_context
import logging
import base64
import time
import threading
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
    communicate(action='heartbeat', retries=COM_INT['max_retries'])


# # Threaded actuation command
# def threaded_communicate(action, retries=None):
#     """Threaded actuation command with retry logic."""
#     hostname = NODE_CONF['hostname']
#     host = '10.132.136.73' #NODE_CONF['ctrl_host']
#     retries = retries
#     endpoint = action
#     ca = get_tls_context().get_ca_certs()
#     api_key = NODE_CONF['api_key'] 
#     action_id = str(uuid.uuid4())
#     url = f"https://{host}/v1/nodes/{hostname}/{endpoint}"
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = json.dumps(NODE_STATUS)
#     data = json.loads(data)
    
#     try:
#         response = requests.post(
#             url=url,
#             json=data,
#             headers=headers,
#             cert=ca,
#             verify=False,
#             timeout=1
#         )
#         print(response.status_code, response.json())
#         if response.status_code == 201:
#             log_message(f"Command {action_id} sent to {hostname}: {action}")
#             json_data = response.json()
            

#             return data

#     except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
#         log_message(f"ERROR: {e} {action_id} to {hostname}. Retrying...")
#         retries -= 1
        
#         if retries > 0:
#             threaded_communicate(endpoint, retries)

def communicate(action, retries=None):
    """Threaded actuation command with retry logic."""
    hostname = NODE_CONF['hostname']
    host = '10.132.136.73'  # NODE_CONF['ctrl_host']
    retries = retries
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
        #logging.debug(f"Response status code: {response.status_code}")
        #logging.debug(f"Response JSON: {response.json()}")

        if response.status_code == 201:
            log_message(f"Command {action_id} sent to {hostname}: {action}")
            var = response.json()
            print(var)
            #COM_INT['next'] = 

    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
        log_message(f"ERROR: {e} {action_id} to {hostname}. Retrying...")
        retries -= 1
        if retries > 0:
            communicate(endpoint, retries)

'''
def communicate(action):
    retries = COM_INT['max_retries']
    """Send communication in a separate thread."""
    thread = threading.Thread(target=threaded_communicate, args=(action, retries)
    )
    thread.daemon = True
    thread.start()
'''