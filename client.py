from gtts import gTTS
from pydub import AudioSegment
import os
import random
import requests
import subprocess
import sys
import time

compliments = ['Good job',
               'Amazing job',
               'Well done',
               'Way to go',
               'Congrats',
               'All hail',
               'Lets hear it for',
               'Too crude to be true',
               'Awesome work',
               'Bravo',
               'Hip hip hooray for']


def create_and_play_mp3(user, title):
    random.seed()
    mytext = 'The card with title: {} is completed. {} {}!'.format(
             title,
             random.choice(compliments),
             user)
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save('text.mp3')

    bing_sound = AudioSegment.from_mp3("bing.mp3")
    speech = AudioSegment.from_mp3("text.mp3")
    applauding = AudioSegment.from_mp3("applaud.mp3")
    total = bing_sound + speech + applauding
    total.export('final.mp3', format="mp3")

    p = subprocess.Popen(["ffplay", "-autoexit", "-nodisp", "final.mp3"])
    p.communicate()
    os.remove('text.mp3')
    os.remove('final.mp3')


if __name__ == "__main__":
    while(1):
        try:
            data = requests.get("http://{}:5000/".format(sys.argv[1])).json()
            create_and_play_mp3(data['user'], data['title'])
        except: # noqa
            pass

        time.sleep(20)
