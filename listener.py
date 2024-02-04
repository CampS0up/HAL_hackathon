# starts a loop that waits for the user to say text containing
# "open the pod doors hal" and then returns the result
# file containing function that will be used for HAL
# to listen to us. this file includes a function that listens
# for him and then returns what he's saying as text


import speech_recognition as sr

should_return = False

def listen():
    MyText = None
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    # Exception handling to handle
    # exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level

            try:
                r.adjust_for_ambient_noise(source2, duration=0.2)
            except Exception as e:
                print(f"error: ambient noise wasn't set{e}")
            #listens for the user's input
            audio2 = r.listen(source2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        r.pause_threshold = 0.5



    return MyText
