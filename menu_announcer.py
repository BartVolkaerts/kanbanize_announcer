from bs4 import BeautifulSoup
import urllib.request
import datetime
from gtts import gTTS
import subprocess

now = datetime.datetime.now()
dayname = now.strftime("%A")

page = urllib.request.urlopen('https://sharedcampus.be/menu.html')
d = page.read()
found_day = False

def parse_menu(menu):
    print(menu)
    menu = menu.split('\n')
    return "De menu van vandaag. Soep: {}, Schotel: {}, Suggestie: {}.".format(menu[1], menu[3], menu[5])


def speak_menu(menu):
    language = 'nl'
    myobj = gTTS(text=menu, lang=language, slow=False)
    myobj.save('menu.mp3')
    p = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "menu.mp3"])
    p.communicate()
    os.remove('menu.mp3')


soup = BeautifulSoup(d, "html.parser")
for tr in soup.findAll("table"):
    for td in tr.find_all("td"):
        if found_day == False:
            if dayname in td.text:
                found_day = True
        else:
            speak_menu(parse_menu(td.text))
            break
    if found_day:
        break
