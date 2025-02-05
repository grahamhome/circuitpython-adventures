import time
import board
import pwmio
from adafruit_motor.motor import DCMotor


# Motor driver connections
motor = DCMotor(
    pwmio.PWMOut(board.GP10, frequency=1000),
    pwmio.PWMOut(board.GP11, frequency=1000),
)

# Motor speed
motor_speed = 0.3

motor.throttle = motor_speed
