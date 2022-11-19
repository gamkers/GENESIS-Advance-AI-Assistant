from features import talk
from features import sounds
from googlesearch import search
import webbrowser
import requests
import re
from halo import Halo
from bs4 import BeautifulSoup
def pearson(my_string):
    query = my_string
    sounds()
    talk("scanning and analysing the user name in social medias")
    talk("check this out sir, i think this is enough to know about a person ")
    pattern = "(instagram|facebook|youtube|twitter|github|linkedin|scholar|hackerrank|tiktok|maps)+\.(com|edu|net|fandom)"

    for i in search(query, tld="co.in", num=15, stop=15, pause=2):
        if (re.search(pattern, i)):
            webbrowser.open(i)
        else:
            print("match not found")

def phnumber(my_string):
    print(my_string)
    phonenum = ("91" + my_string.replace(" ", ""))
    url = ("http://apilayer.net/api/validate?access_key=cd3af5f7d1897dc1707c47d05c3759fd&number=" + phonenum)
    resp = requests.get(url)
    details = resp.json()
    sounds()
    talk("collecting data")
    print('')
    print("Country : " + details['country_name'])
    talk("Country : " + details['country_name'])
    print("Location : " + details['location'])
    talk("Location : " + details['location'])
    print("Carrier : " + details['carrier'])
    talk("Carrier : " + details['carrier'])

def scan_image():
    talk("scaning and analysing the image")
    talk("wait a second sir")
    spinner = Halo(text=' Scanning', spinner='dots')
    image = ("C:/Users/idmak/Pictures/test.jpg")
    try:
        spinner.start()
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }
        url = 'http://www.google.co.in/searchbyimage/upload'
        secondurl = {'encoded_image': (image, open(image, 'rb')), 'image_content': ''}
        response = requests.post(url, files=secondurl, allow_redirects=False)
        fetch = response.headers['Location']

        req = requests.get(fetch, headers=headers)
        socialmedia = ["instagram", "facebook", "twitter", "linkedin", "github"]
        linklist = []
        print("[+] Scan started......")
        talk("Checking whether the image is associated in any social media ")
        print("Scanning started in Instagram")
        print("Scanning started in Github")
        print("Scanning started in Facebook")
        print("Scanning started in Twitter")
        print("Scanning started in Linkedin")
        talk('found some matching result')
        if (req.status_code == 200):
            soup = BeautifulSoup(req.content, 'html.parser')
            for g in soup.find_all('div', class_='g'):
                anchors = g.find_all('a')
                if 'href' in str(anchors[0]):
                    linklist.append(anchors[0]['href'])
            c = 0
            for i in socialmedia:
                sm = str(i)

                for j in linklist:
                    if sm in str(j):
                        c = c + 1
                        print("[+]" + j)

                        webbrowser.open(j)

            if c == 0:
                talk("No social Media links associated with this image")
        spinner.stop()
    except Exception as e:
        webbrowser.open(e)
        print(e)
