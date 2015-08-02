#!/usr/bin/env python3


"""
This example illustrates manipulating a led brightness from a light sensor.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

LED_PIN_PWM = 9  # LED attached to this pin
LDR_PIN = 0  # Light sensor  attached to A0 ("A" is dropped)

# configure the servo
board.set_pin_mode(LDR, Constants.ANALOG)
board.set_pin_mode(LED_PIN_PWM, Constants.PWM)

for x in range(0, 10):
	# read the pot and  output it's value to the led 
	var = (board.analog_read(LDR_PIN))
	board.analog_write(LED_PIN_PWM, int(var/4))
	print ("LDR value is " ,var)
	board.sleep(0.5)

# close the interface down cleanly
board.shutdown()
