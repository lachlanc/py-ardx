

No previous coding experience is required to work through the exercises in this guide. This primer summarises some of the basics of the Python language that we will use to program our Arduinos and should be used more as a reference than a learning source . 

See the [Python 3 documentation](https://docs.python.org/3/) and the <a href="https://github.com/MrYsLab/pymata-aio/wiki">Pymata</a> docs for more detail.


## Variable assignment

    foo = 0;

## Types

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

    import Pymata3
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

    # this is a comment until the end of the line

    
## Writing to the console

    print("Hello World");

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
    	print (j,end=" "s)

returns 4 3 2 1

	i=0
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

## Exception and File handling 

	try:
			f = open(arg, 'r')          # try to do something
		except IOError:
			print 'cannot open', arg  # handle errors
	else:
			print arg, 'has', len(f.readlines()), 'lines'
			f.close()
	finally:   # this block is executed regardless of whether there was an exception
			print 'Goodbye, world!'


