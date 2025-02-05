from time import sleep
import board
from adafruit_hcsr04 import HCSR04
from pwmio import PWMOut
from digitalio import DigitalInOut, Pull

# Part 4 - daily record tracker

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
# How many people have come in?
people_count = 0
# What's the most people we've seen in one day?
people_record = 0  # New code
# Is there a person in the shop right now?
person_in_shop = False
# Main loop
while True:
    if get_distance() < max_distance:
        # We detected a person!
        ding_dong()
        person_detected = False
        if not person_in_shop:
            # A person has entered the shop!
            people_count += 1
            print(f"{people_count} people have entered the shop today")
        # Reset the "person in shop" flag
        person_in_shop = not person_in_shop
    if not toggle_button.value:
        print("Closing time!")
        # New section
        if people_count > people_record:
            print(f"New record! We had {people_count} visitors today.")
            people_record = people_count
        people_count = 0
    sleep(0.1)
    
# Next steps: Talk about / demonstrate sensor & switch debouncing