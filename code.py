# Write your code here :-)
# CircuitPlaygroundExpress_NeoPixel

import time

import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.1)
pixels.fill((0, 0, 0))
pixels.show()

# choose which demos to play
# 1 means play, 0 means don't!
simpleCircleDemo = 0
flashDemo = 0
rainbowDemo = 1
rainbowCycleDemo = 1

RED = 0x110000  # (0x10, 0, 0) also works
YELLOW = (0x10, 0x10, 0)
GREEN = (0, 0x10, 0)
AQUA = (0, 0x10, 0x10)
BLUE = (0, 0, 0x10)
PURPLE = (0x10, 0, 0x10)
BLACK = (0, 0, 0)
WHITE = (16,16,16)

MAIN_COLORS = [WHITE,RED,YELLOW,GREEN,AQUA,BLUE,PURPLE,BLACK]


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - (pos * 3)), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - (pos * 3)), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))


def simpleCircle (wait,colors):

    for j in range(len(colors)):

        for i in range(len(pixels)):
            pixels[i] = colors[j]
            time.sleep(wait)
        time.sleep(wait)

def flashdemofunc (wait,colors):
    print('Flash Demo')

    for j in range(len(colors)):
        pixels.fill(colors[j])
        pixels.show()
        time.sleep(wait)

def rainbow_modes(wait,mode):
    for j in range(255):
        for i in range(len(pixels)):
            if mode == 0:
                idx = int(i + j)
            else:
                idx = int((i * 256 / len(pixels)) + j * 10)
            pixels[i] = wheel(idx & 255)
        pixels.show()
        time.sleep(wait)


while True:
    if simpleCircleDemo:
        print('Simple Circle Demo')
        simpleCircle(0.05,MAIN_COLORS)

    if flashDemo:  # this will play if flashDemo = 1 up above
        print('Flash Demo')
        flashdemofunc(0.5,MAIN_COLORS)


    if rainbowDemo:
        print('Rainbow Demo')
        rainbow_modes(.001,0)

    if rainbowCycleDemo:
        print('Rainbow Cycle Demo')
        rainbow_modes(.001,1)