from gtts import gTTS
import pygame


def text_to_speech(text):
    tts = gTTS(text, lang='en')
    tts.save("speak.mp3")
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('speak.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

    pygame.mixer.music.stop()  # Stop the music
    pygame.mixer.quit()  # Quit the mixer

def play_sound(file):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick rate as needed

    pygame.mixer.music.stop()  # Stop the music
    pygame.mixer.quit()  # Quit the mixer
