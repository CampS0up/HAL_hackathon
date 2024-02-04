import chat
import listener

voice_input = "" #i know this looks silly here but it'll break if you delte this line

while True:
    voice_input = listener.listen()
    if ("open the pod bay doors hal" in voice_input):
        print("I'msorry Dave. I cant do that.")
        break

while True:
    voice_input = listener.listen()
    if voice_input != None:
        response = chat.response(voice_input)
        print("generating response")
        print(response)