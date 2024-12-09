import logging
import time

# Setup logging
logging.basicConfig(filename="logs/ctrl.log", level=logging.INFO)

def log_message(message):
    logging.info(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}")
