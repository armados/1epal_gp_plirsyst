# -*- coding: utf-8 -*-
 
from gtts import gTTS

tts = gTTS('Καλημέρα Κόσμε!', lang='el')

tts.save('1epalaudio.mp3')


tts = gTTS('Hello world!', lang='en')

tts.save('1epalaudio_en.mp3')
