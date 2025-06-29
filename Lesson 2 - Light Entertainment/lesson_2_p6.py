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
    levels = [
        0.3,  # 4 red LEDs, slow speed
        0.25, # 3 red LEDs, faster
        0.2,  # 2 red LEDs, even faster
        0.15  # 1 red LED, fastest
    ]

    for level, delay in enumerate(levels, start=1):
        red_start = level + 1
        red_end = red_start + (4 - level)  # Red area shrinks each level
        direction = 1  # 1 = right, -1 = left
        pos = 0  # Blue dot position

        while True:
            # Move blue dot
            pixels.fill(BLACK)
            for i in range(red_start, red_end + 1):
                pixels[i] = RED
            
            if red_start <= pos <= red_end:
                pixels[pos] = PURPLE  # Turn red+blue = purple
            else:
                pixels[pos] = BLUE

            pixels.show()
            time.sleep(delay)

            # Check button press
            if not button.value:
                if red_start <= pos <= red_end:
                    flash(GREEN, 1)  # Correct press
                    break  # Move to next level
                else:
                    flash(RED, 3)  # Wrong press

            # Update position
            pos += direction
            if pos == 0 or pos == NUM_LEDS - 1:
                direction *= -1  # Bounce off edges

        # Game won
        flash(GREEN, 3)
        pixels.fill(BLACK)
        pixels.show()

# Run the game
game()
# Stop using the LEDs
pixels.deinit()