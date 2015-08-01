<a id="intro"></a>
## ABOUT THIS GUIDE

pyBots are Arduino-based robots that are controlled by [Python](http://Python.org/).

This guide will step you through assembling and programming a number of projects using an Arduino-compatible microcontroller and Python, to help you get started building your own NodeBots. This guide has been designed to be used with the Arduino Experimenter's Kit, which is available from several suppliers, including SparkFun, AdaFruit, SEEED Studio and Freetronics.

The overall goal of the this guide is fun. Beyond this, the aim is to get you comfortable using node.js to control a wide range of electronic components through small, simple and easy circuits. The focus is to get each circuit working then to give you the tools to figure out how it works and how to extend it.

![ARDX](/images/ARDX-cover.jpg "ARDX")


<a id="openhardware"></a>
## ABOUT OPEN SOURCE HARDWARE

This guide has been adapted by [Anna Gerber](https://github.com/AnnaGerber) and [other members of the NodeBots community](https://github.com/AnnaGerber/node-ardx/graphs/contributors) from the SparkFun version of .:oomlout:.'s ARDX (Arduino Experimenter's) Guide.

All of .:oomlout:.'s projects are open source. What does this mean? It means that all of the materials that make up the ARDX kit, including this guide, circuit diagrams and code are available for free download. But it goes further: you're also free to reproduce and modify any of this material, then distribute it for yourself. This is possible because this guide is released under a Creative Commons (CC-BY-SA) license. If you reproduce or modify this guide you must credit SparkFun and .:oomlout:. in your design and share your developments in a similar manner. Why? We grew up learning and playing with open source software and the experience was good fun. We think it would be lovely if a similar experience was possible with physical things.

More details on the Creative Commons CC (By Share Alike) License can be found at [http://ardx.org/CCLI](http://ardx.org/CCLI).

<a id="j5"></a>
## ABOUT PyMATA

We will be working with the [PyMata](https://github.com/MrYsLab/PyMata) library for Python to program our Arduinos. PyMata uses a protocol called [Firmata](http://firmata.org/wiki/Main_Page) to communicate with the microcontroller over USB (Universal Serial Bus).

<a id="firmata"></a>
### Setting Up Firmata

Before you can start programming your Arduino with python, you will need to load Firmata onto your Arduino-compatible microcontroller:

* Download [Arduino IDE](http://arduino.cc/en/main/software)
* Connect your Arduino-compatible microcontroller via USB
* Launch Arduino IDE and open the Firmata sketch via the menu: `File > Examples > Firmata > StandardFirmata`
* Select your Arduino board type (e.g. Arduino Uno) via `Tools > Board`
* Select the port for your board via `Tools > Serial Port > (the comm port of your Arduino)`
* Upload the program by selecting `File > Upload`

If you are having trouble uploading, a full trouble shooting guide can be found here: [http://ardx.org/TRBL](http://ardx.org/TRBL)

<a id="running"></a>
### Running a PyMata program

The PyMata module can be installed on python3  with `pip3 install pymata-aio` already been installed when you installed this guide, so any code examples you create within the node-ardx directory will run.

Run code examples from the terminal e.g.

`python3  code/CIRC01-code-led.py`

## License
    
The source code is available from https://github.com/lachlanc/py-ardx

This work is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported License

To view a copy of this license visit http://creativecommons.org/licenses/by-sa/3.0/

Or send a letter to: Creative Commons<COMMA> 171 Second Street<COMMA> Suite 300<COMMA> San Francisco<COMMA> California 94105<COMMA> USA.
