import keyboard
from utils.logger import log_info

def register_emergency_hotkey(stop_callback):
    """
    Registers Ctrl + Alt + X as an emergency kill switch
    """

    def emergency_stop():
        log_info("EMERGENCY STOP triggered (Ctrl+Alt+X)")
        stop_callback()

    keyboard.add_hotkey("ctrl+alt+x", emergency_stop)
    log_info("Emergency hotkey registered: Ctrl+Alt+X")
