from gtts import gTTS
import playsound


def text_to_speech(text):
    tts = gTTS(text, lang='en')

    tts.save("speak.mp3")
    playsound.playsound("speak.mp3")

# Example usage:
text_to_speech("I wanna die")
