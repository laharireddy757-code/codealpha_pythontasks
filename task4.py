print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hi! How can I help you?")
    
    elif "how are you" in user:
        print("Bot: I'm fine! 😊")
    
    elif "name" in user:
        print("Bot: I am a simple chatbot.")
    
    elif "bye" in user:
        print("Bot: Goodbye! 👋")
        break
    
    else:
        print("Bot: Sorry, I don't understand.")