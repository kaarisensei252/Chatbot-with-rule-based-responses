def simple_chatbot():
    print("Hello! I'm a simple chatbot. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'quit':
            print("Chatbot: Goodbye! Have a nice day.")
            break
            
        elif 'hello' in user_input or 'hi' in user_input:
            print("Chatbot: Hi there! How can I help you?")
            
        elif 'how are you' in user_input:
            print("Chatbot: I'm just a program, but I'm functioning well! How about you?")
            
        elif 'your name' in user_input:
            print("Chatbot: I'm SimpleBot, a rule-based chatbot.")
            
        elif 'time' in user_input or 'date' in user_input:
            from datetime import datetime
            now = datetime.now()
            print(f"Chatbot: The current date and time is {now.strftime('%Y-%m-%d %H:%M:%S')}")
            
        elif 'help' in user_input:
            print("Chatbot: I can respond to greetings, tell you about myself, give the time, or answer simple questions.")
            
        elif 'thank' in user_input:
            print("Chatbot: You're welcome!")
            
        elif 'weather' in user_input:
            print("Chatbot: I'm sorry, I don't have access to weather data.")
            
        elif 'joke' in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
            
        else:
            print("Chatbot: I'm not sure I understand. Could you try asking differently?")

# Start the chatbot
simple_chatbot()