import RPi.GPIO as GPIO
import time

## Setting Value
encoder0pinA = 2                  ##A pin -> the interrupt pin 0
encoder0pinB = 4                  ##B pin -> the digital pin 4

encoder0PinALast = 0
duration = 0                                 ##the number of the pulses
Direction = True                         ##the rotation direction default -> Forward

## Initial IN mode as pull down
GPIO.setmode(GPIO.BCM)
GPIO.setup(encoder0pinA, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(encoder0pinB, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

## Function: when interrupt happen
def wheelSpeed():
	Lstate = GPIO.input(encoder0pinA)
	if encoder0PinALast == 0 and Lstate == 1 :
		val = GPIO.input(encoder0pinB)
		if val == 0 and Direction :
			Direction = False                       //Reverse

		elif val == 1 and ~Direction :
			Direction = True                        //Forward

	encoder0PinALast = Lstate
	if ~Direction :
		duration+1
	else :
		duration-1


## event defination
GPIO.add_event_detect(encoder0pinA, GPIO.RISING, callback = wheelSpeed)

## main loop
try:
	while True:		# repeat
		print "Pulse: %d" % duration
 		duration = 0
		time.sleep(0.1)

except KeyboardInterrupt:		# When push Ctrl + C
	print "STOP"

## End
GPIO.remove_event_detect(encoder0pinA)		# remove event
GPIO.cleanup()
