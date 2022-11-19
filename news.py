import webbrowser
import requests
from features import talk
from features import notification
from features import take_command
import time
from bs4 import BeautifulSoup

def sports_news():
    url = "https://indianexpress.com/section/sports/"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    ##print(data.prettify())
    talk("getting info from top articles")
    temp = data.find_all('h2', class_="title")
    talk("reading top 5 Sports news")
    notification("National News", temp[0].text)
    talk("first" + temp[0].text)
    notification("Sports News ", temp[1].text)
    talk("and second news is " + temp[1].text)
    notification("Sports News ", temp[2].text)
    talk("then third one is " + temp[2].text)
    notification("Sports ", temp[3].text)
    talk("last before one " + temp[3].text)
    notification("Sports ", temp[4].text)
    talk("last but not least " + temp[4].text)
    talk("for more info can i open the website for you sir?")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://indianexpress.com/section/sports/")
    else:
        talk("ok sir")

def gloabl_news():
    url = "https://abcnews.go.com/International/"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    ##print(data.prettify())
    temp = data.find_all('div', class_="News__Content__Container")

    talk("reading top 5 Global news")
    notification("National News", temp[0].text)
    talk("first" + temp[0].text)
    time.sleep(2)
    notification("Global News ", temp[1].text)
    talk("and second news is " + temp[1].text)
    time.sleep(2)
    notification("Global News ", temp[2].text)
    talk("then third one is " + temp[2].text)
    time.sleep(2)
    notification("Global ", temp[3].text)
    talk("last before one " + temp[3].text)
    time.sleep(2)
    notification("Global ", temp[4].text)
    talk("last but not least " + temp[4].text)
    time.sleep(2)
    talk("for more info can i open the website for you sir?")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://abcnews.go.com/International/")
    else:
        talk("ok sir")

def webscrape_TechNews():
    url = "https://gadgets.ndtv.com/news"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    talk("getting info from top articles")

    temp = data.find_all('div', class_="caption_box")
    talk("reading top 5 Tech news")
    notification("Tech News", temp[0].text)
    talk("first" + temp[0].text)
    notification("Tech News ", temp[1].text)
    talk("and second news is " + temp[1].text)
    notification("Tech News ", temp[2].text)
    talk("then third one is " + temp[2].text)
    notification("Tech News ", temp[3].text)
    talk("last before one " + temp[3].text)
    notification("Tech News ", temp[4].text)
    talk("last but not least " + temp[4].text)
    talk("for more info can i open the website for you sir?")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://gadgets.ndtv.com/news")
    else:
        talk("ok sir")

def national_news():
    url = "https://indianexpress.com/section/india/"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    ##print(data.prettify())
    talk("getting info from top articles")
    temp = data.find_all('h2', class_="title")
    talk("reading top 5 National news")
    notification("National News", temp[0].text)
    talk("first" + temp[0].text)
    notification("National News ", temp[1].text)
    talk("and second news is " + temp[1].text)
    notification("National News ", temp[2].text)
    talk("then third one is " + temp[2].text)
    notification("National ", temp[3].text)
    talk("last before one " + temp[3].text)
    notification("National ", temp[4].text)
    talk("last but not least " + temp[4].text)

def latest_news():
    url = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    ##print(data.prettify())
    talk("getting info from top articles")
    temp = data.find_all('h2', class_="newsHdng")
    talk("reading top 5 LATEST news")
    notification("National News", temp[0].text)
    talk("first" + temp[0].text)
    notification("Latest News ", temp[1].text)
    talk("and second news is " + temp[1].text)
    notification("Latest News ", temp[2].text)
    talk("then third one is " + temp[2].text)
    time.sleep(1)
    notification("Latest ", temp[3].text)
    talk("last before one " + temp[3].text)
    time.sleep(1)
    notification("Latest ", temp[4].text)
    talk("last but not least " + temp[4].text)
    talk("for more info can i open the website for you sir?")
    dis = take_command()
    if "yes" in dis:
        talk("opening chrome")
        webbrowser.open_new("https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation")
    else:
        talk("ok sir")

def output(news):
    if "national" in news:
        national_news()
    elif "sports" in news:
        sports_news()
    elif "global" in news:
        gloabl_news()
    elif "tech" in news:
        webscrape_TechNews()
    elif "latest" in news:
        latest_news()
    else:
        print("search not found ")