import board
import neopixel
import time

# Constants
NUM_LEDS = 8
BUTTON_PIN = board.GP20  # Change if using a different pin

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)

# Setup
pixels = neopixel.NeoPixel(board.GP0, NUM_LEDS, brightness=0.3, auto_write=False)

def flash(color, times, delay=0.2):
    """Flash all LEDs a given color a number of times."""
    for _ in range(times):
        pixels.fill(color)
        pixels.show()
        time.sleep(delay)
        pixels.fill(BLACK)
        pixels.show()
        time.sleep(delay)

flash(GREEN, 10)
pixels.deinit()