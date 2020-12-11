import os
from gtts import gTTS

def play(txt):
    text = txt 
    if text == '':
        text = 'please enter something first'

    tts = gTTS(text=f'{text}.\n')

    tts.save('recording.mp3')

    file = 'recording.mp3'
    os.system("mpg123 " + file)