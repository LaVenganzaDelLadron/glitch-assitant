import pyttsx3

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init()

        self.engine.setProperty('rate', 175)

    def say(self, text: str):
        print(f"Assistant: {text}")

        self.engine.say(text)
        self.engine.runAndWait()