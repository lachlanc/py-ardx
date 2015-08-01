#!/usr/bin/env python3

"""
Copyright (c) 2015 Alan Yorinks All rights reserved.
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU  General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.
You should have received a copy of the GNU General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from pymata_aio.pymata3 import PyMata3
from pymata_aio.constants import Constants


def pin_6_pwm_128():
    """
    Set digital pin 6 as a PWM output and set its output value to 128 
    Also sets digital pin 13 as a standard digital write to compare brightness
    @return:
    """
    # instantiate the pymata_core API
    board = PyMata3()
    LED_PIN_PWM = 3;
    LED_PIN=13
    # set the pin mode
    board.set_pin_mode(LED_PIN_PWM, Constants.PWM)
    board.set_pin_mode(LED_PIN, Constants.OUTPUT)

    # minimum pwm value is 0 max is 254
    board.analog_write(LED_PIN_PWM, 50)
    board.digital_write(LED_PIN,1)
    board.sleep(1)
    board.analog_write(LED_PIN_PWM,254)
    board.sleep(1)
    board.analog_write(LED_PIN_PWM,200)

    

    board.sleep(5)

    # reset the board and exit
    board.shutdown()


if __name__ == "__main__":
    pin_6_pwm_128()
