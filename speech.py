import speech_recognition as sp
from time import ctime
import random
import pyttsx3
import playsound 
import os
from gtts import gTTS
import webbrowser
engine = pyttsx3.init()
rec = sp.Recognizer()

def record_voice(ask = False):
    if ask:
        bot_speech(ask)
    with sp.Microphone() as source:
        audio_data = rec.listen(source)
        voice_data = ''
        try:
            text = rec.recognize_google(audio_data)
        except sp.RequestError:
            bot_speech("The speech conversion is down")
        except sp.UnknownValueError:
            bot_speech("The voice cant be detected!")
        return voice_data
def bot_speech(audio_string):
    tts = gTTS(text=audio_string , lang='en')
    r = random.randint(1 , 1000000)
    audio_file = "audio--" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
    
    
    
    
def respond(voice_data):
    if "what is your name" in voice_data:
        bot_speech("My name is ALEXIS")
    if "what is your age" in voice_data:
        bot_speech("I am 16 years old")
    if "search" in voice_data:
        search = record_voice("What can i search for you sir")
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        bot_speech("Here the result for " + search )
    if "find location" in voice_data:
        location = record_voice("What is the location that you are looking for? ")
        url = "https://google.nl/map/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        bot_speech("Here is the location for " + location )
    if "exit" in voice_data:
        exit()
    if "what is your purpose" in voice_data:
        bot_speech("My purpose is to assist you in every thing that i can")
    if "who made you" in voice_data:
        bot_speech("I am made by a self taught software engineer KINFE MICHAEL TARIKU")
    else:
        bot_speech("I have no idea what you are talking about")
    
        

    

bot_speech("what can i help you with? ")
while 1:
    
    voice_data = record_voice()
    respond(voice_data)


        