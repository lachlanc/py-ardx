#!/usr/bin/env python3


"""
This example illustrates manipulating a button motor.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

LED_PIN = 5  #  led attached to this pin
BUTTON_PIN = 6
# configure the servo
board.set_pin_mode(LED_PIN, Constants.OUTPUT)
board.set_pin_mode(BUTTON_PIN , Constants.INPUT)

for x in range(0, 10):
    # move the servo to 20 degrees
    val = board.digital_read(BUTTON_PIN )
    if val = 1:
		print("button is pressed ")
	else:
		print("button isn't pressed ")
    board.digital_write(LED_PIN,val)
    board.sleep(0.5)

# close the interface down cleanly
board.shutdown()
