#speech/listen.py

import speech_recognition as sr

class Listener:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_goole(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            return ""

        except Exception as e:
            print(f"Error {e}")
            return ""