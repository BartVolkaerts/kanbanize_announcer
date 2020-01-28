from bs4 import BeautifulSoup
from gtts import gTTS
import datetime
import os
import random
import subprocess
import urllib.request

now = datetime.datetime.now()
dayname = now.strftime("%A")

page = urllib.request.urlopen('https://sharedcampus.be/menu.html')
d = page.read()

announcements = ['De menu van vandaag',
                 'Vandaag op het menu',
                 'Jammie, vandaag is het']


def parse_menu(menu):
    print(menu)
    menu = menu.split('\n')
    return "{}. {}. {}. Suggestie: {}.".format(random.choice(announcements),
                                               menu[1],
                                               menu[3],
                                               menu[5])


def speak_menu(menu):
    language = 'nl'
    myobj = gTTS(text=menu, lang=language, slow=False)
    myobj.save('menu.mp3')
    p = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "menu.mp3"])
    p.communicate()
    os.remove('menu.mp3')


soup = BeautifulSoup(d, "html.parser")
found_day = False
for tr in soup.findAll("table"):
    for td in tr.find_all("td"):
        if found_day is False:
            if dayname in td.text:
                found_day = True
        else:
            speak_menu(parse_menu(td.text))
            break
    if found_day:
        break
