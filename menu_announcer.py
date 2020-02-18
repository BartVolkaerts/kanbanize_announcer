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
                 'Jammie, vandaag is het',
                 'Vandaag wordt het smullen met',
                 'Vandaag maakt Ivona jullie blij met']


def parse_menu(menu):
    print(menu)
    menu = menu.split('\n')
    random.seed()
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
table = soup.findAll("table")[1].find_all("td")
menu = table[3+(2*datetime.datetime.today().weekday())].text
speak_menu(parse_menu(menu))
