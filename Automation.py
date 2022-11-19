from features import sounds
from keyboard import press
from keyboard import press_and_release
import webbrowser as web
from features import talk
def ChromeAuto(command):
    sounds()
    query = command

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close the tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        tab = tab.replace("to", "")
        tab = tab.replace("in chrome", "")

        num = int(tab)

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("open ", "")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        elif 'whatsapp web' in NameA:

            web.open("https://web.whatsapp.com/")

        else:
            talk("i can get you sir")

def YouTubeAuto(command):
    sounds()
    query = str(command)
    if 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'full screen' in query:
        press('f')
    elif 'film screen' in query:
        press('t')
    elif 'skip' in query:
        press('l')
    elif 'back' in query:
        press('j')
    elif 'previous' in query:
        press_and_release('SHIFT + p')
    elif 'next' in query:
        press_and_release('SHIFT + n')
    elif 'mute' in query:
        press('m')
    elif 'unmute' in query:
        press('m')
    else:
        talk("No Command Found!")