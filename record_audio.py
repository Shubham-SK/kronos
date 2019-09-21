import os

os.system("arecord -D plughw:1 -f cd -vv ~/speech.wav")
