import os
from gtts import gTTS



def play(txt):
    text = txt 
    if text == '':
        text = 'please enter something first'

    tts = gTTS(text=f'{text}.\n')

    tts.save('/home/mmohdbilal/KIVY/KIVY-5/data.mp3')

    file = "/home/mmohdbilal/KIVY/KIVY-5/data.mp3"
    os.system("mpg123 " + file)


