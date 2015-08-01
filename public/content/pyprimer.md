

No previous coding experience is required to work through the exercises in this guide. This primer summarises some of the basics of the Python language that we will use to program our Arduinos and should be used more as a reference than a learning source . 

See the [MDN JavaScript Reference](https:#developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) and <a href="https:#github.com/rwaldron/johnny-five">Johnny-Five</a> docs for more detail.


## Variable assignment

    foo = 0;

## Types
# need to change to more pythonic variable names 
    myInt = 42
    myFloat = 3.1415
    myBoolean = True
    myString = "This is a string"
    myList = [1,2,3]
    myDictionary = {MyField : "Some value" , MyKey : 42}
    # Object instantiation using new
    var myDate = new Date();

## Operators

Numeric operators include + (addition) - (subtraction) / (division) * (multiplication) % (modulo)

    x = 4;
    x = x + 1; # x is 5
    y = x % 2; # y is 1
    x+=1; # x is 6
    x-=1; # x is 5
    x += 3; # x is 8
    print "The value of x is " + x


The `type` operator returns the type
    
    type(aString) # returns <type 'str'>

## Import

Include a library in a python program

    import Pyfirmata
	from math import sqrt
	
The latter just imports the sqrt function from the math library 


## Math
	import math 
	import random 
    math.floor(myfloat) #takes floor of floating point number
    math.ceil(myInt)
    min(x, y) # returns the minimum value of a list or several variables 
    Math.pi
    random.random()  #random number between 0 and up to but not equal to 1

## Comments

    # Comment until the end of the line

    
## Writing to the console

    console.log("Hello World");

## Conditional Behaviour

Use comparison operators < (less than) > (greater than) <= (less than or equal) >= (greater than or equal) == (equals) != (not equals) 

    if x > 0:
		print("x is bigger than 0")
	    
    else:
	    print("x is NOT bigger than 0")
    }

## Loops

    for i in range (0,10):
    	print(i)
    
	i=[4,3,2,1]
    for j in i:
    	print j,;

returns 4 3 2 1

    while (x < 10) {
    	print(x)
    	i+=1
    }

## Functions

    def myIncrementFunction(x):
    	return x + 1
    

## Calling functions

    myIncrementFunction(1000)
returns 1001

Functions defined as part of an Object are known as methods, and can be called as follows:
	import time 
	import calender
	
    time.gmtime()
	calendar.timegm(time.gmtime()) # return time in seconds since unix epoch 
#put link here 
## Exception handling


 try:
        f = open(arg, 'r')          # try to do something
    except IOError:
        print 'cannot open', arg  # handle errors
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
    finally:   # this block is executed regardless of whether there was an exception
        print 'Goodbye, world!'

## Handling events
#how do you do this in python ? 
Use `on` to attach a callback function that will be executed whenever the event occurs:

    var myBoard = new five.Board();
    myBoard.on("ready", function() {
    	# code to be executed when the board is ready
    });

