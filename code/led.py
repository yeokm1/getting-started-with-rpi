import time
import RPi.GPIO as GPIO
#set up GPIO using BCM numbering, alternative is pin numbering
GPIO.setmode(GPIO.BCM)

ledPin = 17

#Initialise pin for output
GPIO.setup(ledPin, GPIO.OUT)

#Create a variable to store current state of LED
ledStatus = False

while True:
	
    #Pause program by one second
    time.sleep(1)
    
    #Set new status to variable
    ledStatus = not ledStatus

    #Write new state to led
    GPIO.output(ledPin, ledStatus)