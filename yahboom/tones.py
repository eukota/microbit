# Experimental file around tones

Tones = {"C3":131, "C#3":139, "D3":147, "D#3":157, "E3":165, "F3":175, "F#3":185, "G3":196, "G#3":208, "A3":220, "A#3":233, "B3":247,
         "C4":262, "C#4":277, "D4":294, "D#4":311, "E4":330, "F4":349, "F#4":370, "G4":392, "G#4":415, "A4":440, "A#4":466, "B4":494,
         "C5":523, "C#5":554, "D5":587, "D#5":622, "E5":659, "F5":698, "F#5":740, "G5":784, "G#5":831, "A5":880, "A#5":932, "B5":988}

def playTone(frequency, duration):
    music.pitch(frequency)
    sleep(duration)
    music.stop()

def playAllTones(duration):
    tone_list = []
    for tone in Tones.items():
        tone_list.append(tone[1])
    tone_list.sort()
    for tone in tone_list:
        playTone(tone,duration)

