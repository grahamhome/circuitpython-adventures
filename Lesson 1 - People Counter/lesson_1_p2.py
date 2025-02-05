from time import sleep
import board
from adafruit_hcsr04 import HCSR04
from pwmio import PWMOut
from digitalio import DigitalInOut, Pull  # New line

# Part 2: Adding a reset button

# Setup
sensor = HCSR04(trigger_pin=board.GP0, echo_pin=board.GP1)
max_distance = 70
buzzer = PWMOut(pin=board.GP22, frequency=440, duty_cycle=0, variable_frequency=True)
toggle_button = DigitalInOut(board.GP21)
toggle_button.switch_to_input(pull=Pull.UP)

# Ding-dong function
def ding_dong():
    # Play G4 for 300 ms
    buzzer.frequency = 392
    buzzer.duty_cycle = 32768  # 50% duty cycle
    sleep(0.3)
    # Play C5 for 400 ms
    buzzer.frequency = 523
    sleep(0.4)
    buzzer.duty_cycle = 0

# Function to get distance
def get_distance():
    try:
        return sensor.distance
    except:
        return max_distance
    
# Variables to keep track of state
# Is there a person in front of the sensor?
person_detected = False
# How many people have we seen?
people_count = 0
# Main loop
while True:
    if get_distance() < max_distance:
        # We detected a person!
        ding_dong()
        person_detected = False
        people_count += 1
        print(f"{people_count} people have entered the shop today")
    # New section - reset button
    if not toggle_button.value:  
        people_count = 0
        print("A new day begins!")
    sleep(0.1)
