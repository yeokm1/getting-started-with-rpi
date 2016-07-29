import time
import RPi.GPIO as GPIO
#set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

ledPin = 17
buttonPin = 23

GPIO.setup(ledPin, GPIO.OUT)

#This mode requires an external pull down resistor
GPIO.setup(buttonPin, GPIO.IN)

#Set up button pin for input with internal pull down resistor
#Button pin goes to ground if not pressed.
#GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

ledStatus = False

while True:
	
    #Get button input
    input_state = GPIO.input(buttonPin)

    #Change status only if pressed
    if input_state == True:
          ledStatus = not ledStatus
          GPIO.output(ledPin, ledStatus)