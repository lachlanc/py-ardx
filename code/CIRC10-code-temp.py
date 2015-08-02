#!/usr/bin/env python3
"""
This example illustrates reading an analog temperature sensor .
"""
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants
# instantiate PyMata with a 2 second start up delay to allow an Uno to complete its reset
board = PyMata3(2)

TEMP_SENSOR = 0  # temperature sensor is  attached to Analog pin 0

# configure the servo
board.set_pin_mode(TEMP_SENSOR, Constants.ANALOG)
for x in range(0, 3):
    # move the servo to 20 degrees
    raw = board.analog_read(TEMP_SENSOR)
    
    print ("raw output voltage =",raw/1024*5,"V")
    #  the arduino returns the voltage as a 10-bit
    # number where 1024 is max voltage (in our case 5v)
    # and 0 is min voltage (Ov)
    
    # NEED TO ADD CONVERSION HERE 
    cel=((raw * 0.4882814) - 50) #TMP36 conversion to Celsius 
    print ("temperature is",cel,"C")
    #print ("temperature is", ((5.0 * raw * 100.0)/1024.0),"C"); # LM35 temp sensor
    board.sleep(3)

# close the interface down cleanly
board.shutdown()
