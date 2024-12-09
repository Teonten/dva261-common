import logging
import time
from config.settings
# Setup logging
logging.basicConfig(filename="logs/{HOSTNAME}.log", level=logging.INFO)

def log_message(message):
    logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")
