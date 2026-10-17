"""
A simple rule-based chatbot. It reads what the user types, checks it
against a set of rules using if-elif, and replies with a predefined
answer. The chat continues until the user says goodbye.
"""

from datetime import datetime


def get_response(user_input):
    """Returns the chatbot's reply for a given message."""
    message = user_input.lower().strip()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message in ("how are you", "how are you?"):
        return "I'm fine, thanks!"
    elif message in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple chatbot built with Python."
    elif message in ("what can you do", "help"):
        return "I can say hello, chat a little, tell you the time, and say goodbye."
    elif message in ("what time is it", "time"):
        return "It's " + datetime.now().strftime("%H:%M") + " right now."
    elif message in ("thanks", "thank you"):
        return "You're welcome!"
    elif message in ("bye", "goodbye", "exit", "quit"):
        return "Goodbye!"
    elif message == "":
        return "Say something and I'll reply."
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Chatbot:", reply)

        if reply == "Goodbye!":
            break


if __name__ == "__main__":
    main()
