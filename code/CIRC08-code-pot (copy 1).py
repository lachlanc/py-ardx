#!/usr/bin/env python3


"""
This example illustrates manipulating a servo motor.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

SERVO_MOTOR = 5  # servo attached to this pin

# configure the servo
board.set_pin_mode(2, Constants.ANALOG)
board.set_pin_mode(12, Constants.INPUT)

for x in range(0, 3):
    # move the servo to 20 degrees
    print (board.digital_read(12))
    print (board.analog_read(2))
    board.sleep(3)

# close the interface down cleanly
board.shutdown()