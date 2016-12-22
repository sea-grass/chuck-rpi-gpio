#!/usr/bin/python

# Input on BCM 3, button
# When BCM 3 is toggled, it will send a positive signal on BCM 4

# Output on BCM 4, 3.3v

import RPi.GPIO as GPIO

def toggleOutput(channel):
	global num, do_turn_on
	print("Button pressed!")
	num = num + 1
	# toggle the output
	do_turn_on = not do_turn_on
	GPIO.output(4, do_turn_on)
# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN)
GPIO.setup(4, GPIO.OUT)


# track number of key presses
num = 0
do_turn_on = False

GPIO.output(4, do_turn_on)
GPIO.add_event_detect(3, GPIO.RISING, callback=toggleOutput, bouncetime=300)

while num < 4:
	print("Num at " + str(num))
	if (do_turn_on):
		print("output is on")
	else:
		print("output is off")
GPIO.cleanup()
