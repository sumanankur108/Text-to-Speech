import gtts
import playsound

# User Input
answer = input("Enter a statement to convert into speech (press 'Q' to quit): ")

# Text to speech, conversion, and playing
sound = gtts.gTTS(answer, lang="en")
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")
