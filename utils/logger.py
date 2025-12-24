import logging
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "assistant.log")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_info(message: str):
    logging.info(message)
