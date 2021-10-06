# -*- coding: utf-8 -*-
 
from gtts import gTTS

tts = gTTS('Καλημέρα Κόσμε!', lang='el')

tts.save('1epalaudio.mp3')
