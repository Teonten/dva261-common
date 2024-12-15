import logging
import time
from config.settings import NODE_CONF
# Setup logging
logging.basicConfig(filename=f"/usr/local/dva261-common/logs/{NODE_CONF['hostname']}.log", level=logging.INFO)

def log_message(message):
    logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")
