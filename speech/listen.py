# speech/listen.py

from faster_whisper import WhisperModel
import tempfile
import sounddevice as sd
from scipy.io.wavfile import write


class Listener:
    def __init__(self):
        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def listen(self):
        duration = 5
        sample_rate = 16000

        print("Listening...")

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as f:

            write(
                f.name,
                sample_rate,
                recording
            )

            segments, _ = self.model.transcribe(
                f.name
            )

        text = " ".join(
            segment.text
            for segment in segments
        )

        print(f"You: {text}")

        return text.strip() 