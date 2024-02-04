#HAL_hackathon(speaker.py_text to speech)
from gtts import gTTS
import io

def text_to_speech(text):
    tts = gTTS(text=text_en, lang='en')
   #tts = gTTS(text=text_es, lang='es')
    #tts = gTTS(text=text_fr, lang='fr')
    #tts = gTTS(text=text, lang='tlh')

    tts.save("speak.mp3")
    os.system("mpg321 output.mp3")

text_en = "Hello, how are you?"
#text_es = "Hola, este es un mensaje en español."
#text_fr = "Bonjour, ceci est un message en français."
text_to_speech(text_en)
#text_to_speech(text_es)
#text_to_speech(text_fr)
