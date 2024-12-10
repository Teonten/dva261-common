from gevent.pywsgi import WSGIServer
from app import app
from app.client import heartbeat
from config.settings import NODE_CONF
from config.tls_config import get_tls_context
import logging
from signal import pause
from app import actuators


if __name__ == "__main__":
    logging.info(f"Starting {NODE_CONF['hostname']} API server...")
    context = get_tls_context()
    #button.when_activated = button_pressed
    #ultrasonic.when_in_range = sensor_trigger
    #ultrasonic.when_out_of_range = 
    heartbeat()
    http_server = WSGIServer((NODE_CONF['host_ip'], NODE_CONF['host_port']), app, ssl_context=context)
    http_server.serve_forever()
    pause()
