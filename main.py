from chatbot import ChatBot

if __name__ == '__main__':
    chatbot = ChatBot('Tom')

    chatbot.train([
        "Hi, can I help you?",
        "Sure, I'd like to book a flight to Iceland.",
        "Your flight has been booked."
    ])
