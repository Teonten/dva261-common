#!/bin/bash
import gpiozero
from gevent.pywsgi import WSGIServer
from app import app
from app.sensors import ultra_in, ultra_out, button_pressed
from app.client import heartbeat
import config.settings
from config.tls_config import get_tls_context
import logging
#from app import actuators
from signal import pause




if __name__ == "__main__":
    print(f"Starting {config.settings.NODE_CONF['hostname']} API server...")
    logging.info(f"Starting {config.settings.NODE_CONF['hostname']} API server...")
    context = get_tls_context()
    config.settings.BUTTON.when_activated = button_pressed
    config.settings.ULTRASONIC.when_in_range = ultra_in
    config.settings.ULTRASONIC.when_out_of_range = ultra_out

    http_server = WSGIServer((config.settings.NODE_CONF['host_ip'], config.settings.NODE_CONF['host_port']), app, ssl_context=context)
    http_server.serve_forever()
    heartbeat()
    pause()


