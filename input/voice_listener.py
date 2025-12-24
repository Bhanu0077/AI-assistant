import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer
from utils.logger import log_info
from utils.paths import project_path

class VoiceListener:
    def __init__(self, enabled=True):
        self.enabled = enabled
        self.q = queue.Queue()

        model_path = project_path("models", "vosk-en-small")
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

        log_info(f"VoiceListener initialized (enabled={self.enabled})")

    def enable(self):
        self.enabled = True
        log_info("VoiceListener enabled")

    def disable(self):
        self.enabled = False
        log_info("VoiceListener disabled")

    def _audio_callback(self, indata, frames, time, status):
        if status:
            log_info(f"Audio status: {status}")
        self.q.put(bytes(indata))

    import queue

    def listen(self, should_run_callable) -> str | None:
        if not self.enabled:
            return None

        log_info("Listening for voice input (push-to-talk: hold SPACE)")

        try:
            with sd.RawInputStream(
                samplerate=16000,
                blocksize=8000,
                dtype="int16",
                channels=1,
                callback=self._audio_callback
            ):
                while should_run_callable():
                    try:
                        data = self.q.get(timeout=0.5)  # NON-BLOCKING WAIT
                    except queue.Empty:
                        continue

                    if self.recognizer.AcceptWaveform(data):
                        result = json.loads(self.recognizer.Result())
                        text = result.get("text", "").strip()
                        if text:
                            log_info(f"Voice input received: {text}")
                            return text
        except KeyboardInterrupt:
            log_info("Voice listening interrupted safely")

        return None
