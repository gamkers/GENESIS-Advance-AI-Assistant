from pygame import mixer
from pyttsx3 import Engine
import speech_recognition as sr
import pyttsx3
import pygame
from time import sleep
from pynotifier import Notification
import datetime

listener = sr.Recognizer()
engine: Engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 171)
engine.setProperty('volume', 150)
pygame.init()
mixer.music.load("C://Users//idmak//Music//intro0.mp3")
mixer.music.play()
mixer.music.set_volume(50)
engine.runAndWait()
sleep(4)
reminders = "Nothing"



def sounds():
    mixer.music.load("C://Users//idmak//Music//intro2.mp3")
    mixer.music.play()
    mixer.music.set_volume(0.2)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said : {query}")

    except:
        return ""

    query = str(query)
    return query.lower()

def notification(title, desc):
    Notification(
        title=title,
        description=desc,
        duration=5,
        urgency='normal'
    ).send()
def intro():

    sounds()
    ampm = datetime.datetime.now().strftime('%p')
    hour = datetime.datetime.now().strftime('%I')
    hour = int(hour)
    if "AM" in ampm:
        talk("hello sir, good morning")
    elif "PM" in ampm and hour < 4:
        talk("hello sir, good afternoon ")
    elif "PM" in ampm and hour > 3:
        talk("hello sir, good evening")
    else:
        talk("good night")

    time = datetime.datetime.now().strftime('%I:%M %p')
    notification("Time", 'Current time is ' + time)
    talk('Current time is ' + time)

    talk("how can i help you sir")
