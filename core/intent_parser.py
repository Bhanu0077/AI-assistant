from utils.logger import log_info

class IntentParser:
    def __init__(self):
        log_info("IntentParser initialized")

    def parse(self, text: str) -> dict:
        """
        Convert raw text into a structured intent.
        This is a rule-based skeleton (no AI yet).
        """

        text = text.lower().strip()
        log_info(f"Parsing intent from text: {text}")

        # ---- BASIC RULES (expand later) ----

        if text.startswith("open "):
            app = text.replace("open ", "").strip()
            return {
                "action": "open_app",
                "target": app
            }

        if text.startswith("close "):
            app = text.replace("close ", "").strip()
            return {
                "action": "close_app",
                "target": app
            }

        if text in ["exit", "stop", "quit"]:
            return {
                "action": "stop_assistant"
            }

        # ---- UNKNOWN COMMAND ----
        return {
            "action": "unknown",
            "raw_text": text
        }
