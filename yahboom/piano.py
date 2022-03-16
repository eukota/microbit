from microbit import *
import music
from random import randint
import neopixel
rgb = neopixel.NeoPixel(pin1,4)

class Piano():
    """Piano class to interface with the Yahboom Piano board
       YB-MMM02 VER:1.2
    """
    def __init__(self):
        self.octave = 3

        # Keys are stored in single bit addressing
        self.keys = {"M" :0b0000000000000001,
                     "L" :0b0000000000000010,
                     "C" :0b0000000000000100,
                     "CD":0b0000000000001000,
                     "D" :0b0000000000010000,
                     "DE":0b0000000000100000,
                     "E" :0b0000000001000000,
                     "F" :0b0000000010000000,
                     "FG":0b0000000100000000,
                     "G" :0b0000001000000000,
                     "GA":0b0000010000000000,
                     "A" :0b0000100000000000,
                     "AB":0b0001000000000000,
                     "B" :0b0010000000000000,
                     "H" :0b0100000000000000
                     }

        # Preset tones for 3 octaves
        self.tones = {"C":{3:131,4:262,5:523},
                      "CD":{3:139,4:277,5:554},
                      "D":{3:147,4:294,5:587},
                      "DE":{3:157,4:311,5:622},
                      "E":{3:165,4:330,5:659},
                      "F":{3:175,4:349,5:698},
                      "FG":{3:185,4:370,5:740},
                      "G":{3:196,4:392,5:784},
                      "GA":{3:208,4:415,5:831},
                      "A":{3:220,4:440,5:880},
                      "AB":{3:233,4:466,5:932},
                      "B":{3:247,4:494,5:988}
                      }
        
        # Some basic colors
        self.colors = {"red":[255,0,0],"green":[0,255,0],"blue":[0,0,255]}
        
        # Init i2c
        i2c.init(freq=100000,sda=pin20,scl=pin19)

    def playTone(self, frequency, duration=250):
        """Play a tone at frequency for duration milliseconds"""
        music.pitch(frequency)
        sleep(duration)
        music.stop()

    def ShowRGB(self, RGB, duration=0):
        """Show the specified RGB color for duration milliseconds across all LEDs on the board"""
        for rgb_id in range(0,4):
            rgb[rgb_id] = (RGB[rgb_id][0],RGB[rgb_id][1],RGB[rgb_id][2])
            rgb.show()
        if duration > 0:
            sleep(duration)
            self.ClearRGB()
    
    def GetColor(self, color:str):
        """Provide some popular colors"""
        red = 0
        green = 0
        blue = 0
        if color == "red":
            red = 255
        elif color == "green":
            green = 255
        elif color == "blue":
            blue = 255
        else:
            return self.Color()
        for rgb_id in range(0,4):
            rgb[rgb_id] = (red,green,blue)
        return rgb

    def ClearRGB(self):
            rgb.clear()

    def Color(self):
        """Generate a random RGB color"""
        for rgb_id in range(0,4):
            red = randint(0, 30)
            green = randint(0, 30)
            blue = randint(0, 30)
            rgb[rgb_id] = (red,green,blue)
        return rgb

    def readTouch(self):
        """Read the touch output of the piano via the i2c bus"""
        i2c.write(0x50,bytearray([8]))
        a=i2c.read(0x50,1)
        b=i2c.read(0x50,1)
        return b[0]*256 + a[0]
        
    def PlayPiano(self):
        """Play the piano once for the currently selected touch"""
        keyval = self.readTouch()
        if bool(keyval&self.keys["L"]):
            self.octave = 3
            self.ShowRGB(self.GetColor("red"))
            return
        if bool(keyval&self.keys["M"]):
            self.octave = 4
            self.ShowRGB(self.GetColor("green"))
            return
        if bool(keyval&self.keys["H"]):
            self.octave = 5
            self.ShowRGB(self.GetColor("blue"))
            return
        for key in self.keys.items():
            if bool(keyval&key[1]):
                self.playTone(self.tones[key[0]][self.octave])
                self.ShowRGB(self.Color())
                break
    
    def run(self):
        """Runs the PlayPiano() function in a loop"""
        while True:
            if button_a.is_pressed():
                display.show(Image.HAPPY)
                while True:
                    self.PlayPiano()
                    if button_b.is_pressed():
                        display.show(Image.HEART) # back to not running
                        break
            sleep(500)
            if button_b.is_pressed():
                display.show(Image.SAD) # bye!
                break

# Show it is working
display.show(Image.HEART)
p = Piano()
p.run()





