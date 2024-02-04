import pygame
import time

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Example usage:
mp3_file_path = "C:\Users\ktenn\OneDrive\Documents\New folder\HAL_hackathon\daisy.mp3"
play_mp3(mp3_file_path)