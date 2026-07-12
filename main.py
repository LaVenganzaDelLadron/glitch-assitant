# main.py

from speech.listen import Listener
from speech.speak import Speaker

from ai.ollama_provider import OllamaProvider
from ai.prompts import build_chat_prompt


def main():
    listener = Listener()
    speaker = Speaker()

    llm = OllamaProvider()

    speaker.say("Glitch Assistant is online.")

    while True:
        user_input = listener.listen()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit", "shutdown"]:
            speaker.say("Goodbye.")
            break

        prompt = build_chat_prompt(user_input)

        try:
            response = llm.generate(prompt)

            print(f"\nAssistant: {response}\n")

            speaker.say(response)

        except Exception as e:
            error = f"Error: {e}"

            print(error)

            speaker.say("Something went wrong.")


if __name__ == "__main__":
    main()