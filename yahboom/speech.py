# Playing with speech commands
from microbit import *
import speech
def runSpeech():
    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            break
        if button_a.is_pressed():
            speech.say("Hello Edward")
        if button_b.is_pressed():
            speech.say("oh my god")