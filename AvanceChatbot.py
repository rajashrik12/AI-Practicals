# Advanced Rule-Based Chatbot using intent classification

def get_response(user_input):
    user_input = user_input.lower()

    # Define sample intents and keywords
    responses = {
        "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
        "goodbye": ["bye", "goodbye", "see you", "exit"],
        "thanks": ["thank you", "thanks", "thx"],
        "products": ["product", "items", "catalog", "show me products"],
        "price": ["price", "cost", "how much", "rate"],
        "support": ["support", "help", "customer care", "service"]
    }

    answers = {
        "greeting": "Hello! How can I help you today?",
        "goodbye": "Goodbye! Have a great day!",
        "thanks": "You're welcome! 😊",
        "products": "We offer electronics, clothing, and accessories. What are you interested in?",
        "price": "Our prices range from ₹500 to ₹50,000 depending on the product.",
        "support": "You can reach our support at support@example.com or call 1800-123-456."
    }

    # Identify intent
    for intent, keywords in responses.items():
        for keyword in keywords:
            if keyword in user_input:
                return answers[intent]

    # Default reply
    return "I'm sorry, I didn't quite get that. Could you please rephrase?"

# Main chatbot loop
def chatbot():
    print("🤖 Advanced Chatbot: Hello! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if 'exit' in user_input.lower():
            print("Bot: It was nice chatting with you. Bye! 👋")
            break
        response = get_response(user_input)
        print("Bot:", response)

chatbot()
