#
import RPi.GPIO as GPIO
import time
from time import sleep
# Debug Settings
GPIO.setwarnings(False)
debug_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if debug_messages : print("Debug Message are 'ON'")
else : print("Debug Message are 'OFF'")
hardware_test_messages = 1 # If debug messages is 1 then message will be printed, else if 0 they will be silenced
if hardware_test_messages : print("Hardware Test Message are 'ON'")
else : print("Hardware Test Message are 'OFF'")    
# Makey Bot Pin Assignments
GPIO.setmode(GPIO.BOARD) # Note This is specifying the physical pins on the Raspberry Pi Header

redRGBPin = 11
greenRGBPin = 13
blueRGBPin = 15
redRGBPin2 = 16
greenRGBPin2 = 18
blueRGBPin2 = 22
GPIO.setup(redRGBPin,GPIO.OUT)
GPIO.setup(greenRGBPin,GPIO.OUT)
GPIO.setup(blueRGBPin,GPIO.OUT)
GPIO.setup(redRGBPin2,GPIO.OUT)
GPIO.setup(greenRGBPin2,GPIO.OUT)
GPIO.setup(blueRGBPin2,GPIO.OUT)


#choosing a frequency for pwm
Freq = 1000

#defining the pins that are going to be used with PWM
REDRGB = GPIO.PWM(redRGBPin, Freq)  
GREENRGB = GPIO.PWM(greenRGBPin, Freq)
BLUERGB = GPIO.PWM(blueRGBPin, Freq)
REDRGB2 = GPIO.PWM(redRGBPin2, Freq)  
GREENRGB2 = GPIO.PWM(greenRGBPin2, Freq)
BLUERGB2 = GPIO.PWM(blueRGBPin2, Freq)

#lighting up the pins. 100 means giving 100% to the pin
REDRGB.start(60)
GREENRGB.start(30)
BLUERGB.start(50)
REDRGB2.start(60)
GREENRGB2.start(30)
BLUERGB2.start(50)

def rghCheck(rgb):
    if hardware_test_messages : print("rgb = ",rgb)
    
    my_color_dic = {"RED":"FF:00:00", "GREEN":"00,FF:00","BLUE":"00:00:FF"}
    for color in my_color_dic:
        print(color)
        if color == rgb:
            print(rgb)
        return rgb
def rgbWrite(r,g,b):
    REDRGB.ChangeDutyCycle(r) 
    GREENRGB.ChangeDutyCycle(g) 
    BLUERGB.ChangeDutyCycle(b)
    REDRGB2.ChangeDutyCycle(r) 
    GREENRGB2.ChangeDutyCycle(g) 
    BLUERGB2.ChangeDutyCycle(b)

# Ask the user which LEDs to turn on or off
led_color = input("Enter LED color (red, yellow, green): ")
led_state = input("Enter state (on or off): ")

# Control the LEDs based on user input
if led_color == "red":
    # Control the red LED
    if led_state == "on":
        # Turn on the red LED
        print("Turning on the red LED")
    elif led_state == "off":
        # Turn off the red LED
        print("Turning off the red LED")
    else:
        print("Invalid state. Please enter 'on' or 'off'.")

elif led_color == "yellow":
    # Control the yellow LED
    if led_state == "on":
        # Turn on the yellow LED
        print("Turning on the yellow LED")
    elif led_state == "off":
        # Turn off the yellow LED
        print("Turning off the yellow LED")
    else:
        print("Invalid state. Please enter 'on' or 'off'.")

elif led_color == "green":
    # Control the green LED
    if led_state == "on":
        # Turn on the green LED
        print("Turning on the green LED")
    elif led_state == "off":
        # Turn off the green LED
        print("Turning off the green LED")
    else:
        print("Invalid state. Please enter 'on' or 'off'.")

else:
    print("Invalid LED color. Please choose from 'red', 'yellow', or 'green'.")