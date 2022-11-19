import os
import sys
import psutil
from applications import *
from news import *
from social_engineering import *
from webscrap import *
from Automation import *
from playsound import playsound
import screen_brightness_control as sbc
import wikipedia
import random
import subprocess
import pyjokes
from nta import *
from codder import codder

intro()
reminders = "Nothing"
def remind(remind0):
    global reminders
    reminders = remind0



def run_genesis():
    command = take_command()

    if 'play' in command:
        talk("what song do you want to play sir")
        song = take_command()
        sounds()
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif "translate" in command:
        webscrap_translate(command)
    elif"wake up" in command:
        sbc.set_brightness(100)
        intro()
    elif 'time' in command:
        sleep(1)
        time = datetime.datetime.now().strftime('%I:%M %p')
        notification("Time", 'Current time is ' + time)
        talk('Current time is ' + time)
    elif 'your name' in command or "who are you" in command:
        sounds()
        talk('im genesis and im a virtual artificial intelligence developed to assist with your task since best i can . ')
    elif "what is" in command:
        webscrap_search(command)
    elif "which is" in command:
        webscrap_search(command)
    elif "offers" in command:
        amazon_offers()
    elif 'who is' in command or "do you know about" in command:
        person = command.replace('who is', '').replace("do you know about", '')
        info = wikipedia.summary(person, 1)
        notification("information", info)
        talk(info)
    elif 'what can you do' in command:
        talk(
            'i can say the current time , weather , i can play songs from youtube , i can search anything on google or wikipedia , i do some maths, i can open apps for you, set a reminder, know about a person and many more')

    elif "i am back" in command:

        playsound("C://Users//idmak//Music//intro1.mp3")

    elif "notes" in command or "files" in command or "data" in command:
        talk("sure sir. i can do it for you. please say the title or topic sir ")
        que = take_command()
        talk("collecting data from the internet")
        answer_finder(que)
        talk("check this out sir")
    elif "ppt" in command or "presentations" in command:
        talk("sure sir. i can do it for you. please say the title or topic sir ")
        que = take_command()
        talk("collecting data from the internet")
        ppt_finder(que)
        talk("check this out sir")


    elif 'good morning' in command:
        wishes = ["Wishing you a very Good Morning!  A new blessing, a new hope, a new light and a new day is waiting for you to conquer it.","A very Good Morning! I hope this morning brings a bright smile on your face. May you have a beautiful and rewarding day! Always keep smiling.","Life is a mystery and things always look impossible until it is made. Do not stop, move ahead and kill it. Good Morning, have a nice day!","Good Morning! It is a bright day. Wake up every morning with an assurance that you can do it. Think positive, stay happy and keep going"]
        talk(random.choice(wishes))

    elif 'good afternoon' in command:
        wishes = ["I wish you a lovely afternoon and a beautiful day.","Wishing for your afternoon to be wonderful, cozy, and happy. Have a great one, dear.","May this afternoon bring a lot of pleasant surprises for you and fills your heart with infinite joy. Wishing you a very warm and love-filled afternoon!","May your Good afternoon be light,blessed,enlightened,productive and happy."]
        talk(random.choice(wishes))

    elif 'good evening' in command:
        wishes = ["Good evening! I hope you had a good and productive day. Cheer up!","No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.","No matter how bad your day has been, the beauty of the setting sun will make everything serene. Good evening.","I am wishing you an amazing evening full of gossips and coffee. Just know that you are always in my mind. Enjoy this evening to the fullest!"]
        talk(random.choice(wishes))

    elif 'good night' in command:
        wishes = ["You have so many reasons to thank God, but first thank him for such a peaceful night like this. What a blissful night for a good sleep. Good night!","May you have sound sleep and wake up tomorrow with new hopes and a lot of positive energy. Good night to you!","Wishing you good night and rest well, dear friend. Stop worrying about life. I will always have your back no matter what.","May tomorrow be sunny and full of joy. Good night!"]
        talk(random.choice(wishes))

    elif 'open chrome' in command:
        sounds()
        talk('opening chrome for you sir')
        subprocess.call('C://Program Files (x86)//Google//Chrome//Application//chrome.exe')

    elif 'office' in command:
        sounds()
        talk('opening office for you sir')
        print('opening office for you sir')
        subprocess.call('C://Users//idmak//AppData//Local//Kingsoft//WPS Office//ksolaunch.exe')

    elif 'search' in command:
        talk("what you want to search sir")
        my_string = take_command()
        sounds()
        talk('ok sir ill search that for you in google')
        print('oks ir ill search that for you in google')
        pywhatkit.search(my_string.replace('search', ''))

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif "reminder" in command:
        sounds()
        talk("what you want to remind sir")

        remind0 = take_command()

        talk("ok sir i remind that")

        remind(remind0)

    elif "remind me" in command:
        global reminders
        talk("yes sir you said to remind" + reminders)

    elif "can you calculate" in command:
        talk("what you want to calculate sir")
        my_string = take_command()
        calc(my_string)

    elif 'hello' in command:
        sounds()
        talk("hi sir, how was the day")

    elif 'sad' in command or 'bad' in command or 'nothing much' in command:
        wishes = ["i wish to have a arms to hug you and say, iam there for you","Please don’t be sad","A certain darkness is needed to see the stars.","Don’t let little stupid things break your happiness","Breathe. It’s only a bad day, not a bad life"]
        talk(random.choice(wishes))
        talk("can i play a song for you sir?")
        des = take_command()
        if "yes" in des:
            options = ["https://www.youtube.com/watch?v=403FGqa-Uv8","https://www.youtube.com/watch?v=pgN-vvVVxMA","https://www.youtube.com/watch?v=wnHW6o8WMas"]
            webbrowser.open_new(random.choice(options))
        else:
            talk("ok sir")

    elif 'happy' in command or 'good' in command:
        wishes = ["im so glad to hear from you sir, your smile make me happy too","im so glad to hear from you sir,Be happy for this moment. This moment is your life","im so glad to hear from you sir,The best way to pay for a lovely moment is to enjoy it","im so glad to hear from you sir,Sometimes your joy is the source of your smile, but sometimes your smile can be the source of your joy"]
        talk(random.choice(wishes))
        talk("can i play a song for you sir?")
        des = take_command()
        if "yes" in des:
            webbrowser.open_new("https://www.youtube.com/watch?v=tQ0yjYUFKAE")
        else:
            talk("ok sir")

    elif 'angry' in command:
        wishes = ["calm down sir, no matter how angry you get , you end up forgiving the people you love","calm down sir,The smarter you get, the more you realize anger is not worth it","Never waste a minute thinking about people you don’t like. Dwight D. Eisenhower"]
        talk(random.choice(wishes))

    elif 'sing' in command:
        talk('I see treeeees of greeeen. red roses tooooo, I watch them bloooom for me and you . And I think to '
             'myself. what a wonderful wooorld')

    elif 'classroom' in command:
        sounds()
        talk("opening google class room for you sir")
        webbrowser.open_new("https://classroom.google.com/h")

    elif 'work to do' in command or "to do" in command:
        sounds()
        talk("sir you have some assignments to do")
        talk("do i open it for you sir")
        des = take_command()
        if "yes" in des:
            webbrowser.open_new("https://classroom.google.com/a/not-turned-in/all")
        else:
            talk("ok sir")

    elif "image" in command:
        talk("okay sir")
        sounds()
        scan_image()

    elif 'discord' in command:
        sounds()
        talk("opening discord")
        web.open("https://discord.gg/cT8ZAqcg")

    elif 'google meet' in command:
        sounds()
        talk("opening google meet sir")

        webbrowser.open_new("https://meet.google.com/lookup/gzbdzqag3p?authuser=0&hs=179")

    elif 'check my whatsapp' in command or "whatsapp message" in command:
        sounds()
        talk("sir you have some messages can i open it for you")
        des = take_command()
        if "yes" in des:
            talk("opening whatsapp")
            startfile('C:\\Users\\idmak\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
            sleep(5)
        else:
            talk("ok sir")

    elif 'instagram' in command:
        web.open("https://www.instagram.com/")

    elif 'in youtube' in command:
        talk("ok sir")
        YouTubeAuto(command)

    elif 'in chrome' in command:
        talk("ok sir")
        ChromeAuto(command)

    elif "close chrome" in command or "close the chrome" in command:
        sounds()
        talk("closing")
        os.system("taskkill /im chrome.exe /f")
    elif "who created you" in command:
        talk("im virtual artificial intelligence developed by sir Akash to assist with some task which programmed by him ")

    elif ' gmail' in command:
        sounds()
        talk("opening gmail sir")
        webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

    elif 'write' in command or 'hand written' in command:
        text_to_handrwitten()

    elif 'read my mind' in command:
        mind_game()

    elif 'awesome' in command:
        talk("thank you sir")

    elif 'thank you' in command or "thanks" in command:
        talk("its my pleasure sir")

    elif 'mail' in command:
        talk("ok sir ill do it for you")
        mail()

    elif "you doing" in command:
        response = ["I’m doing great (thanks). How about you?", "Doing good. You?", 'Doing pretty good. You?']
        talk(random.choice(response))

    elif 'how are you' in command:
        response = ["I’m good, thanks. You?","I’m pretty good. What’s new with you?","Never been better. What about you?"]
        talk(random.choice(response))

    elif 'i am fine' in command:
        talk("happy to hear that sir , how can i help you?")

    elif "wait a minute" in command or "minute" in command:
        talk("im always here to help you")

    elif 'trace' in command or 'track' in command:
        talk("say the phone number sir ill trace for you")
        my_string = take_command()
        phnumber(my_string)

    elif 'want to know about' in command:
        talk("can i help you sir , whom you want to know about")
        my_string = take_command()
        pearson(my_string)

    elif "type" in command:
        talk("ok sir ill type for you, what you want to type sir")
        text = take_command()
        write(text)

    elif 'send a message to' in command:
        name = command.replace("send a message to ", "")
        talk("whats the message sir")
        message = take_command()
        WhatsappMsg(name, message)

    elif 'call to' in command:
        name = command.replace("make a call to ", "")
        talk("ok sir ill connect the call")
        WhatsappCall(name)

    elif 'connect a video with' in command:
        name = command.replace("connect a video with ", "")
        talk("ok sir ill connect the call")
        WhatsappChat(name)

    elif 'how much power left' in command or "how much power we have" in command or "battery" in command:
        battery = psutil.sensors_battery()
        per = battery.percent
        talk(f"sir your system have{per} percent battery")
        if per >= 75:
            talk("we have enough juice to continue our work")
        elif per>=40 and per<=75:
            talk("not yet full but its ok , we have enough power for couple of hours")
        elif per<=15 and per<=30:
            talk("we dont have enough power to manage. please connect your charger")
        elif per>15:
            talk("system in critical stage. please connect to charging or else the system will shutdown in few minutes")

    elif "ipl scores" in command:
        ipl_score()

    elif "news" in command:
        talk("Please choose your category")
        news = take_command()
        output(news)

    elif "hi" in command or "hay" in command:
        intro()

    elif "are you there" in command:
        talk("YEs sir, how can i help you")

    elif "wish me" in command:
        wishes = ["wish you happy life","wishing you all the best","im so proud of you","i wish you luck","You've worked hard for this, i believe in you "]
        talk(random.choice(wishes))
    elif "dice" in command:
        options = [1,2,3,4,5,6]
        talk(random.choice(options))

    elif "coin" in command:
        options = ["head","tail"]
        talk(random.choice(options))


    elif "worst" in command:
        talk("sorry sir, im doing my best")


    elif"your bad"in command:
        talk("Sorry sir , i will try to change")

    elif 'sleep' in command:
        talk("bye sir, have a good day")
        sys.exit()

    elif 'network' in command:
        sounds()
        talk("scaning and analysing the network")
        main()
    elif"coding" in command:
        talk("Yes sir, im learning but still i can help you, how can i help you sir?")
        codder()


    elif '' in command:
        print('still listening....')


    else:
        talk('sorry sir i did not get you.')
        print('sorry sir i did not get you.')

while True:
    run_genesis()
