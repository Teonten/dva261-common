from gevent.pywsgi import WSGIServer
from app import app
from config.tls_config import get_tls_context
import logging
from config.tls_config import get_tls_context

if __name__ == "__main__":
    logging.info("Starting CTRL API server...")
    context = get_tls_context()
    http_server = WSGIServer(("192.168.0.4", 443), app, ssl_context=context)
    http_server.serve_forever()
