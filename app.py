from gevent.pywsgi import WSGIServer
from app import app
from config.settings import HOST_IP
from config.tls_config import get_tls_context
import logging
from signal import pause
from app import actuators


if __name__ == "__main__":
    logging.info("Starting CTRL API server...")
    context = get_tls_context()
    button.when_activated = button_pressed
    ultrasonic.when_in_range = sensor_trigger
    ultrasonic.when_out_of_range = 
    http_server = WSGIServer((HOST_IP, 443), app, ssl_context=context)
    http_server.serve_forever()
    pause()
