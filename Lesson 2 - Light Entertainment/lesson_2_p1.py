import board
import neopixel
import digitalio
import time

# Constants
NUM_LEDS = 8
BUTTON_PIN = board.GP20

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GREEN = (0, 255, 0)

# Setup
pixels = neopixel.NeoPixel(board.GP0, NUM_LEDS, brightness=0.3, auto_write=False)
button = digitalio.DigitalInOut(BUTTON_PIN)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

pos = 0  # Blue dot position - try changing it!

# Turn off all pixels
pixels.fill(BLACK)

# Turn on blue pixel - try changing the color!
pixels[pos] = BLUE
pixels.show()

# Wait 5 seconds (try changing the time!)
time.sleep(5)

# Stop using the LEDs
pixels.deinit()
