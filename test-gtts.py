# -*- coding: utf-8 -*-
 
from gtts import gTTS

tts = gTTS('Καλημέρα Κόσμε!', lang='el')

tts.save('mp3s/1epalaudio.mp3')


tts = gTTS('Hello world!', lang='en')

tts.save('mp3s/1epalaudio_en.mp3')



tts = gTTS('welcome to 1epal pyrgou!', lang='en')

tts.save('mp3s/1epalaudio_en2.mp3')

