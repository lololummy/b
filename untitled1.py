from tkinter import *
import speach_recognition as sr
import pyttsx3
from datetime import datetime


root = tk
root.geometry("500x500")

text_to_speech=pyttsx3

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speak("How can i help you")
    speech_recognisor= sr.Recogniser
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data= speech_recognisor.recognize_google(audio, language='en-in')
        except sr.UnknownValueError:
             print('please repeat i did not get that')
             speak("please repeat i did not get that")
             
             respond(voice_data)
    print(voice_data)
    
        
    
def respond(voice_data):
    voice_data = voice_data.lower
    print(voice_data)
    if "name" in voice_data:
        speak("My name is koolboiy182012 like and subscribe")
        print('My name is koolboiy182012 like and subscribe')
        
    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)
        
      
r_audio()

root.mainloop