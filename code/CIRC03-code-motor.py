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


def pin_9_motor():
    """
    Set digital pin 13 as a output and make it turn on
    @return:
    """
    # instantiate the pymata_core API
    board = PyMata3()
    MOTOR_PIN=9
    # set the pin mode
    board.set_pin_mode(MOTOR_PIN, Constants.OUTPUT)
    board.digital_write(MOTOR_PIN,1)
    board.sleep(3)
    board.digital_write(MOTOR_PIN,0)
    board.sleep(1)
    board.digital_write(MOTOR_PIN,1)
   # wait for 5 seconds to see the MOTOR lit
    board.sleep(3)

    # reset the board and exit
    board.shutdown()

if __name__ == "__main__":
    pin_13_flash()
