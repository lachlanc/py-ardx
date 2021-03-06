
To this point we have controlled light, motion, and
electrons. Let's tackle sound next. But sound is an
analog phenomena, how will our digital Arduino cope?
We will once again rely on its incredible speed which will let it
mimic analog behaviour. To do this, we will attach a piezo element to one of the Arduino's digital pins. A piezo element makes a clicking sound each time it is pulsed with current. If we pulse it at the right frequency (for example 440 Hz (times a second) to make the note middle A) these clicks will run together to produce notes.


<a id="parts"></a>
## Parts

* 2 pin header x 4
* Piezo element
* jumper wires

<a id="circuit"></a>
## Circuit Layout
[<img style="max-width:400px" src="../../images/circ/CIRC06-sheet-small.png" alt="Circuit Layout"/>](../../images/circ/CIRC06-sheet.png)

<a id="assembly"></a>
## Circuit Assembly
![Assembly Diagram](../../images/assembly/CIRC-06-3dexploded.png "Assembly Diagram")

Assembly video: http://ardx.org/VIDE06

<a id="code"></a>
## Code

You can find this code in `code/CIRC-06-code-tone.py`

	from pymata_aio.pymata3 import PyMata3
	from pymata_aio.constants import Constants
	
	
	# create a PyMata instance
	board = PyMata3(2)
	PIN = 9
	board.play_tone(PIN, Constants.TONE_TONE, 100, 1000)
	board.sleep(2)
	board.play_tone(PIN, Constants.TONE_TONE, 1000, 500)
	board.sleep(2)
	board.play_tone(PIN, Constants.TONE_TONE, 500, 500)
	board.sleep(1)
	board.play_tone(PIN, Constants.TONE_NO_TONE, 1000, 500)
	
	
	board.shutdown()
	


<a id="troubleshooting"></a>
## Troubleshooting

### No Sound
Given the size and shape of the piezo element it is easy to miss the right holes on the breadboard. Try double checking its placement.

### Can't Think While the Notes are Playing?
Just pull up the piezo element whilst you think, run the program then plug it back in.


<a id="extending"></a>
## Extending the Code


<a id="more"></a>
## More

For more details on this circuit, see http://ardx.org/CIRC06
