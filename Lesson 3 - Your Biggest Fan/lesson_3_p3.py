import time
import board
import pwmio
import digitalio
from adafruit_motor.motor import DCMotor


# Motor driver connections
motor = DCMotor(
    pwmio.PWMOut(board.GP10, frequency=1000),
    pwmio.PWMOut(board.GP11, frequency=1000),
)

# Setup buttons
speed_button = digitalio.DigitalInOut(board.GP20)
speed_button.direction = digitalio.Direction.INPUT
speed_button.pull = digitalio.Pull.UP  # Use internal pull-up

direction_button = digitalio.DigitalInOut(board.GP21)
direction_button.direction = digitalio.Direction.INPUT
direction_button.pull = digitalio.Pull.UP  # Use internal pull-up

# Motor speeds (off, slow, medium, fast) as PWM duty cycles
motor_speeds = [0, 0.3, 0.6, 0.9]  # PWM duty cycle for DC motor

# Current speed setting
speed_selector = 0
# Is motor spinning forwards (1) or backwards (-1)
direction = 1

def wait_for_release(button):
    """Debounce and wait for button release."""
    time.sleep(0.05)
    while not button.value:
        time.sleep(0.05)


while True:
    if not speed_button.value:  # Button 1 pressed
        speed_selector = (speed_selector + 1) % 4
        print(f"Setting motor speed to {direction * motor_speeds[speed_selector]}")
        motor.throttle = direction * motor_speeds[speed_selector]
        wait_for_release(speed_button)

    if not direction_button.value:  # Button 2 pressed
        direction = direction * -1
        print(f"Setting motor speed to {direction * motor_speeds[speed_selector]}")
        motor.throttle = direction * motor_speeds[speed_selector]
        wait_for_release(direction_button)
        

    time.sleep(0.1)
