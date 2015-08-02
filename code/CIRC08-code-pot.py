#!/usr/bin/env python3


"""
This example illustrates manipulating a led brightness from a pot.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

LED_PIN = 9  # LED attached to this pin
POT_PIN = 0  # potentiometer  attached to A0 ("A" is dropped)

# configure the pins
board.set_pin_mode(POT_PIN, Constants.ANALOG)
board.set_pin_mode(LED_PIN, Constants.PWM)

for x in range(0, 3):
	# read the pot and  output it's value to the led 
	var = (board.analog_read(POT_PIN))
	board.analog_write(LED_PIN, int(var/4))
	print ("pot value is " ,var)
	board.sleep(3)

# close the interface down cleanly
board.shutdown()
