def chatbot():
    print("Hello! I'm your chatbot.Type 'bye' to exit");
    while True:
        data=input("You:")
        data=data.lower()
        if(data=="hi" or  data=="hello"):
            print("Bot:Hi! How can i help you")
        elif(data=="how are u" or data=="how are you"):
            print("Bot:I'm running at full speed and ready to help you shine")
        elif(data=="what is your name"):
            print("Bot:I'm a python chatbot")
        elif(data=="bye"):
            print("Bot:Goodbye! Have a great day")
            break
        else:
            print("Bot:Sorry,I didn't understand u please enter valid data");
chatbot()