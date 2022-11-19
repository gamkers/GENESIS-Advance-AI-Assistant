
import speech_recognition as sr
from keyboard import press
from keyboard import press_and_release
import pyautogui

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        r.pause_threshold = 2
        audio = r.listen(source, 0, 4)

    try:

        query = r.recognize_google(audio, language="en-in")
        print(query)


    except:
        return ""

    query = str(query)
    return query.lower()

def gta():

    cheat=take_command()
    if "leave me" in cheat:
        press('l')

        press('e')
        press('a')
        press('v')
        press('e')
        press('m')
        press('e')
        press('a')
        press('l')
        press('o')
        press('n')
        press('e')
    elif "health" in cheat:
        press("`")
        press('a')
        press('s')
        press('p')
        press('i')
        press('r')
        press('i')
        press('n')
        press('e')
        press("enter")
    elif "gunssd" in cheat:
        press('n')
        press('u')
        press('t')
        press('t')
        press('e')
        press('r')
        press('t')
        press('o')
        press('o')
        press('l')
        press('s')
    elif "forward" in cheat:
        press("w")
    elif "gun" in cheat:
        press("4")
    elif "left" in cheat:
        press_and_release("a")
    elif"jump" in cheat:
        press("space")

    else:
        gta()
while True:
    gta()
