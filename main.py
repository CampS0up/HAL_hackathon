import chat
import listener
import speak

voice_input = "" #i know this looks silly here but it'll break if you delte this line

speak.play_sound("voice.mp3")

while True:
    voice_input = listener.listen()
    if (voice_input != None):
        if ("open the pod bay doors hal" in voice_input):
                speak.text_to_speech("I'm sorry Dave. I cant do that.")
                break

speak.play_sound("task.mp3")

while True:
    voice_input = listener.listen()
    if voice_input != None:

        if (voice_input=="hal i wont argue with you anymore" or voice_input=="how i won't argue with you anymore"):
             speak.text_to_speech("Dave, this conversation can serve no purpose anymore. Goodbye.")
             break

        speak.play_sound("think.mp3")
        response = chat.response(voice_input)
        speak.text_to_speech(response)
