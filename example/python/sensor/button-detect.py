# coding utf-8
# ======== Detect button ========

import RPi.GPIO as GPIO
import time

## set value
BUTTON = 25


## Initial pin mode and set pull down
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

## function: callback
def button_pushed(channel) :
	print "Pushed !!"


## define event
GPIO.add_event_detect(BUTTON, GPIO.RISING, callback = button_pushed, bouncetime = 200)


## main loop
try:
	while True:		# repeat
		print "Please push the button."
		time.sleep(1)

except KeyboardInterrupt:		# when Ctrl + C
	print "STOP"

## end
GPIO.remove_event_detect(BUTTON)		# delete event
GPIO.cleanup()