import pyttsx3

# Initializing the library
text_speech = pyttsx3.init()

# Text input and speech synthesis
while True:
    # User Input
    answer = input("Enter a statement to convert to speech (press 'q' to quit): ")

    # Check if the user wants to quit
    if answer.lower() == 'q':
        break

    # Text-to-Speech Conversion
    text_speech.say(answer)
    text_speech.runAndWait()

# Clean up resources
text_speech.stop()