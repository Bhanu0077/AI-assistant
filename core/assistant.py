import time
from utils.logger import log_info

class Assistant:
    def __init__(self):
        self.running = True
        log_info("Assistant initialized")

    def run(self):
        log_info("Assistant started (headless mode)")
        while self.running:
            time.sleep(1)  # placeholder loop
