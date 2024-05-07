#
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # Note:physical pins 
#GPIO.setwarnings(False)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(40,GPIO.IN)

while(True):
    print(GPIO.input(40))
    GPIO.output(5,GPIO.input(40))