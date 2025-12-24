import sounddevice as sd
import numpy as np
import whisper
from utils.logger import log_info

class WhisperVoiceListener:
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.model = whisper.load_model("base")
        log_info("WhisperVoiceListener initialized (offline)")

    def listen(self) -> str | None:
        if not self.enabled:
            return None

        log_info("Listening (Whisper)… speak now")

        duration = 4  # seconds
        samplerate = 16000

        audio = sd.rec(
            int(duration * samplerate),
            samplerate=samplerate,
            channels=1,
            dtype=np.float32
        )
        sd.wait()

        result = self.model.transcribe(audio.flatten(), fp16=False)
        text = result["text"].strip().lower()

        if text:
            log_info(f"Whisper recognized: {text}")
            return text

        return None
