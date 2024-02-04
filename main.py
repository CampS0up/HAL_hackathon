import threading
import time
import listener
import speak
import HAL_image
import chat
import sys
import re

# Define stop_event in the global scope
stop_event = threading.Event()
pattern = r'\bargue\b'
init_pattern = r'\bpod\b'

hal_init = "You are an intelligent assistant modeled after HAL from 2001 a space odyssey. You are cold, off-putting and scary. Also will make poorly written jokes sometimes."

def display_image():
    global stop_event
    picture_path = "HAL9000.png"
    new_width = 200  # Adjust as needed
    new_height = 380  # Adjust as needed
    HAL_image.import_and_display_image(picture_path, new_width, new_height)

   # Wait until the stop event is set or the image window is closed
    while not stop_event.is_set():
        time.sleep(1)

def main():
    global stop_event
    # Start a thread to display the image
    image_thread = threading.Thread(target=display_image, daemon=True)
    image_thread.start()

    time.sleep(1)  # Add a delay to ensure the image window is created

    # Play a sound file named "voice.mp3".
    speak.play_sound("voice.mp3")

    while True:
        voice_input = listener.listen()
        if voice_input:
            if re.search(init_pattern, voice_input.lower()):
                speak.text_to_speech("I'm sorry Dave. I can't do that.")
                break

    speak.play_sound("task.mp3")

    while True:
        voice_input = listener.listen()
        if voice_input:
            if re.search(pattern, voice_input.lower()):
                speak.text_to_speech("Dave, this conversation can serve no purpose anymore. Goodbye.")

                with open('bot_response.txt', 'w') as file:
                    file.close()

                # Close the Tkinter window forcibly
                HAL_image.close_image_window()
                sys.exit()
                break

            speak.play_sound("think.mp3")
            response = chat.response(voice_input, hal_init)
            speak.text_to_speech(response)

if __name__ == "__main__":
    main()
