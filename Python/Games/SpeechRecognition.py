import speech_recognition as sr 
#from getts import gTTS
#import os
#voice =""
#while True:
r = sr.Recognizer()
with sr.Microphone() as source:
    print("say something...")

    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
            
    except:
        print("say something...")
#hr = gTTs(text=voice, Lang='en', slow= flase)
#hr.save("1.wav")
