# Simple Chatbot
# Handles basic user greetings and questions.

def chatbot():
    print("Hello! Welcome to our customer support.")
    while True:
        user_input = input("You: ").lower()

        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hi there! How can I help you today?")
        elif 'price' in user_input:
            print("Bot: Our products range from $10 to $1000. What are you looking for?")
        elif 'bye' in user_input or 'exit' in user_input:
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Can you please rephrase?")

chatbot()
