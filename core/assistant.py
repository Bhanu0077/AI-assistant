import time
from utils.logger import log_info
from utils.hotkeys import register_emergency_hotkey

class Assistant:
    def __init__(self):
        self.running = True
        log_info("Assistant initialized")

        # Register emergency stop
        register_emergency_hotkey(self.stop)

    def stop(self):
        log_info("Assistant stopping safely")
        self.running = False

    def run(self):
        log_info("Assistant started (headless mode)")
        while self.running:
            time.sleep(1)

        log_info("Assistant stopped")
