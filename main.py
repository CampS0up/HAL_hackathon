import chat
import listener

voice_input = listener.listen()
chat.response(voice_input)