responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hey! What's on your mind?",
    "how are you": "I'm doing great, thanks! How about you?",
    "what is your name": "I'm Chatty, your friendly chatbot!",
    "goodbye": "See you later! Have a great day!",
    "thanks": "You're welcome!",
    "default": "I didn't understand that. Can you please rephrase?"
}

def process_input(user_input):
    user_input = user_input.lower()  
    for key in responses:
        if key in user_input:
            return responses[key]
    return responses["default"]  

# Start the chatbot
print("Welcome to Chatty! I'm here to help.")
while True:
    user_input = input("You: ")
    response = process_input(user_input)
    print("Chatty: " + response)