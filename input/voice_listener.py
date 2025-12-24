from utils.logger import log_info

class VoiceListener:
    def __init__(self, enabled=True):
        self.enabled = enabled
        log_info(f"VoiceListener initialized (enabled={self.enabled})")

    def enable(self):
        self.enabled = True
        log_info("VoiceListener enabled")

    def disable(self):
        self.enabled = False
        log_info("VoiceListener disabled")

    def listen(self) -> str | None:
        """
        TEMPORARY STUB.
        Later this will return text from microphone.
        """
        if not self.enabled:
            return None

        # ---- SIMULATED VOICE INPUT ----
        simulated_input = "open notepad"
        log_info(f"Voice input received (simulated): {simulated_input}")
        return simulated_input
