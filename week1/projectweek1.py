responses = {
    'hello': 'Hi there!',
    'how are you?': 'I am doing well, thank you!',
    'what is your name?': 'I am a simple chatbot.',
    'how can you help me ?': "I can answer simple questions and have a conversation with you.",
    'bye': 'Goodbye!'
}

while True:
    raw_input = input("Enter the prompt:")
    clean_input = raw_input.lower().strip()
    reply = responses.get(clean_input, "sorry,i dont understand.")
    print(reply)

    if clean_input == "exit":
        break
