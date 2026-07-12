from speech.listen import Listener
from speech.speak import Speaker

listener = Listener()
speaker = Speaker()

while True:
    text = listener.listen()

    if not text:
        continue

    if text.lower() == "exit":
        break

    speaker.say(f"You said {text}")