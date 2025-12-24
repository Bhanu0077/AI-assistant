import time
from utils.logger import log_info
from utils.hotkeys import register_emergency_hotkey
from core.intent_parser import IntentParser

class Assistant:
    def __init__(self):
        self.running = True
        self.intent_parser = IntentParser()

        log_info("Assistant initialized")
        register_emergency_hotkey(self.stop)

    def stop(self):
        log_info("Assistant stopping safely")
        self.running = False

    def handle_text_command(self, text: str):
        intent = self.intent_parser.parse(text)
        log_info(f"Intent parsed: {intent}")

        # TEMPORARY handling (no execution yet)
        if intent["action"] == "stop_assistant":
            self.stop()

    def run(self):
        log_info("Assistant started (headless mode)")

        # TEMP input simulation (remove later)
        test_commands = [
            "open notepad",
            "close chrome",
            "stop"
        ]

        for cmd in test_commands:
            if not self.running:
                break
            self.handle_text_command(cmd)
            time.sleep(1)

        while self.running:
            time.sleep(1)

        log_info("Assistant stopped")
