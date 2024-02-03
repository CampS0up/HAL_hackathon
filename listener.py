# file containing function that will be used for HAL
# to listen to us. this file includes a function that listens
# for him and then returns what he's saying as text

import speech_recognition as sr
import pyttsx3


while(1):    
     
    # Exception handling to handle
    # exceptions at the runtime
    try:
         
        # use the microphone as source for input.
        with sr.Microphone() as source2:
                
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            sr.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input 
            audio2 = sr.listen(source2)
             
            # Using google to recognize audio
            MyText = sr.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say ",MyText)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
