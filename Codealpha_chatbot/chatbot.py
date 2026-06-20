def chatbot():
    print("🤖 ChatBot Started")
    print("Type 'bye' to exit.")

    while True:
        user = input("\nYou: ").lower()

        if user == "hello":
            print("Bot: Hi! How can I help you?")

        elif user == "how are you":
            print("Bot: I am fine, thanks!")

        elif user == "what is your name":
            print("Bot: I am a Python ChatBot.")

        elif user == "who created you":
            print("Bot: I was created by a CodeAlpha Intern.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()