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
lastPressedTime = time.time()

while True:

    #Get button input
    input_state = GPIO.input(buttonPin)

    #Get current time
    currentTime = time.time()

    #Change status only if pressed and time is greater than 0.2s threshold -> Debouncing
    if input_state == True and (currentTime - lastPressedTime) >= 0.2:
    	lastPressedTime = currentTime
    	ledStatus = not ledStatus
    	GPIO.output(ledPin, ledStatus)