import time
from utils.logger import log_info
from utils.hotkeys import register_emergency_hotkey
from core.intent_parser import IntentParser
from security.permission_engine import PermissionEngine
from security.confirmation import ConfirmationEngine
from input.voice_listener import VoiceListener


class Assistant:
    def __init__(self):
        self.running = True
        self.intent_parser = IntentParser()
        self.voice_listener = VoiceListener(enabled=True)
        self.confirmation_engine = ConfirmationEngine()

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
    def handle_text_command(self, text: str):
        intent = self.intent_parser.parse(text)
        log_info(f"Intent parsed: {intent}")

        action = intent.get("action")
        decision = self.permission_engine.check(action)

        if decision == "deny":
            log_info(f"Action denied: {action}")
            return

        if decision == "confirm_twice":
            confirmed = self.confirmation_engine.confirm_twice(action)
            if not confirmed:
                log_info(f"Action aborted after failed confirmation: {action}")
                return

            log_info(f"Action confirmed twice: {action}")
            return  # execution later

        if decision == "allow":
            log_info(f"Action allowed: {action}")

            if action == "stop_assistant":
                self.stop()


    def run(self):
        log_info("Assistant started (headless mode)")

        while self.running:
            text = self.voice_listener.listen()
            if text:
                self.handle_text_command(text)
                time.sleep(1)  # cooldown

        log_info("Assistant stopped")



    

