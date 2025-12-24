import time
from utils.logger import log_info
from utils.hotkeys import register_emergency_hotkey
from core.intent_parser import IntentParser
from security.permission_engine import PermissionEngine
from input.voice_listener import VoiceListener


class Assistant:
    def __init__(self):
        self.running = True
        self.intent_parser = IntentParser()
        self.voice_listener = VoiceListener(enabled=True)

        self.permission_engine = PermissionEngine(
            "config/default_policy.json",
            "config/user_policy.json"
        )

        log_info("Assistant initialized")
        register_emergency_hotkey(self.stop)

    def stop(self):
        log_info("Assistant stopping safely")
        self.running = False

    def handle_text_command(self, text: str):
        intent = self.intent_parser.parse(text)
        log_info(f"Intent parsed: {intent}")

        action = intent.get("action")
        decision = self.permission_engine.check(action)

        if decision == "deny":
            log_info(f"Action denied: {action}")
            return

        if decision == "confirm_twice":
            log_info(f"Action requires double confirmation: {action}")
            return  # confirmation logic comes later

        if decision == "allow":
            log_info(f"Action allowed: {action}")

            # TEMP handling only
            if action == "stop_assistant":
                self.stop()
                
    def handle_voice_input(self):
        text = self.voice_listener.listen()
        if text:
            self.handle_text_command(text)

    def run(self):
        log_info("Assistant started (headless mode)")

        while self.running:
            self.handle_voice_input()
            time.sleep(2)

        log_info("Assistant stopped")


    

