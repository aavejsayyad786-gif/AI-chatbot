print("🤖 Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("🤖 Chatbot: Hello! How can I help you?")
    
    elif "your name" in user:
        print("🤖 Chatbot: I am a simple AI Chatbot.")
    
    elif "how are you" in user:
        print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")
    
    elif "help" in user:
        print("🤖 Chatbot: I can answer basic questions like greetings.")
    
    elif user == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 👋")
        break
    
    else:
        print("🤖 Chatbot: Sorry, I didn't understand that.")