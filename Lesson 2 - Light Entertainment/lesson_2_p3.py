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

def flash(color, times, delay=0.3):
    """Flash all LEDs a given color a number of times."""
    for _ in range(times):
        pixels.fill(color)
        pixels.show()
        time.sleep(delay)
        pixels.fill(BLACK)
        pixels.show()
        time.sleep(delay)

def game():
    delay=0.3
    direction = 1  # 1 = right, -1 = left
    pos = 0  # Blue dot position

    while True:
        # Move blue dot
        pixels.fill(BLACK)

        pixels[pos] = BLUE

        pixels.show()
        time.sleep(delay)

        # Update position
        pos += direction
        if pos == 0 or pos == NUM_LEDS - 1:
            direction = direction * -1  # Bounce off edges

# Run the game
game()
# Stop using the LEDs
pixels.deinit()
