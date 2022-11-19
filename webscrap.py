from features import sounds
import requests
from features import talk
from features import notification
from features import take_command
import webbrowser
from time import sleep
import pywhatkit
from PIL import Image
from bs4 import BeautifulSoup
import re
from googlesearch import search

def webscrap_translate(command):
    sounds()
    search = command
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find('div', class_="PME8Xe MUxGbd gbj1yb WZ8Tjf", id="lrtl-transliteration-text")
    print(temp.text)
    talk(temp.text)

def webscrap_search(command):
    sounds()
    search = command
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    notification("information", temp)
    talk(temp)

def ipl_score():
    search = "ipl scores"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    sounds()
    talk("collecting and analysing data ")
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find_all('div', class_="BNeawe tAd8D AP7Wnd")
    notification("IPL SCORES", temp[1].text)
    talk("in previous match " + temp[1].text)
    notification("IPL SCORES", temp[3].text)
    talk("last before match " + temp[3].text)
    notification("IPL SCORES", temp[5].text)
    talk("2 matches before " + temp[5].text)
    talk("for more info can i open the website for you sir?")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://www.google.com/search?q=ipl+score")
    else:
        talk("ok sir")


def amazon_offers():
    url = "https://www.grabon.in/amazon-deals/"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    sounds()
    talk("collecting offer details from amazon")
    temp = data.find_all("div", class_="g-deal")
    talk("ill send the Deals of the day , in the notification sir")
    notification("Deal of the day", temp[0].text.replace("   ", "on").replace("BUY NOW", "BEFORE OFFER PRICE"))
    sleep(4)
    talk("collecting, and sending you the offers")
    notification("Deal of the day", temp[1].text.replace("   ", "on").replace("BUY NOW", "BEFORE OFFER PRICE"))
    sleep(6)
    notification("Deal of the day", temp[2].text.replace("   ", "on").replace("BUY NOW", "BEFORE OFFER PRICE"))
    sleep(6)
    talk("for more info can i open the website for you sir")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://www.grabon.in/amazon-deals/")
    else:
        talk("ok sir")

def text_to_handrwitten():
    talk('Yes sir, i try my best')
    talk("say YOUR TITLE SIR")
    title = take_command()
    print(title)
    search = title
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    sounds()
    talk("analysing the matching result with the title from the database")
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    passage = temp
    talk("wait a second sir")
    pywhatkit.text_to_handwriting(title + "\n" + passage, 'C:\\Users\\idmak\\Pictures\\handwritten\\output7.png', [10, 10, 10])
    talk("match found")
    sounds()
    notification("information", temp)
    talk("writing" + passage)
    img = Image.open('C:\\Users\\idmak\\Pictures\\handwritten\\output7.png')
    img.show()

def answer_finder(que):
    que1=que+"filetype:pdf"
    for i in search(que1, tld="co.in", num=5, stop=10, pause=2):
        if (re.search("pdf", i)):
            webbrowser.open(i)
        else:
            print("match not found")
def ppt_finder(que):
    que1=que+"filetype:ppt"
    for i in search(que1, tld="co.in", num=3, stop=3, pause=2):
        if (re.search("ppt", i)):
            webbrowser.open(i)
        else:
            print("match not found")

