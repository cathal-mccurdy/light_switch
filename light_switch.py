import RPi.GPIO as GPIO
import time
#imports libraies needed

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.IN,GPIO.PUD_UP)
#sets up the GPIO pins

while True:
    if GPIO.input(11) == 0:
        GPIO.output(7,True)
    #this turns on an LED if the button is pressed
        
    else:
        GPIO.output(7,False)
    #this turns it off if it's not pressed
        
