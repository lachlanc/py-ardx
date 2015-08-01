VOUT=10mv/°F×T

#!/usr/bin/env python3


"""
This example illustrates reading a LM whatever a servo motor.
"""

from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

TEMP_SENSOR = 2  # servo attached to this pin

# configure the servo
board.set_pin_mode(TEMP_SENSOR, Constants.ANALOG)
for x in range(0, 3):
    # move the servo to 20 degrees
    raw = board.analog_read(TEMP_SENSOR)
    print ("raw output voltage =",raw/1024*5,"V")
    #  the arduino returns the voltage as a 8-bit
    # number where 1024 is max voltage (in our case 5v)
    # and 0 is min voltage (Ov)
    
    # NEED TO ADD CONVERSION HERE 
    
    print (board.analog_read(2))
    board.sleep(3)

# close the interface down cleanly
board.shutdown()
