from utils.logger import log_info

class ConfirmationEngine:
    def __init__(self):
        log_info("ConfirmationEngine initialized")

    def confirm_twice(self, action: str) -> bool:
        """
        TEMP confirmation logic.
        Later: voice + gesture / PIN.
        """

        log_info(f"Confirmation requested for action: {action}")

        # ---- FIRST CONFIRM ----
        first = self._ask_confirmation(step=1)
        if not first:
            log_info("First confirmation failed")
            return False

        # ---- SECOND CONFIRM ----
        second = self._ask_confirmation(step=2)
        if not second:
            log_info("Second confirmation failed")
            return False

        log_info("Double confirmation successful")
        return True

    def _ask_confirmation(self, step: int) -> bool:
        """
        TEMP stub.
        """
        log_info(f"Waiting for confirmation step {step}")

        # Simulated confirmation (always YES for now)
        simulated_response = "yes"

        if simulated_response.lower() == "yes":
            log_info(f"Confirmation step {step} accepted")
            return True

        return False
