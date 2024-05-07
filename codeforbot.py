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
red_pin = 29
yellow_pin = 31
green_pin = 37

GPIO.setup(redRGBPin,GPIO.OUT)
GPIO.setup(greenRGBPin,GPIO.OUT)
GPIO.setup(blueRGBPin,GPIO.OUT)
GPIO.setup(redRGBPin2,GPIO.OUT)
GPIO.setup(greenRGBPin2,GPIO.OUT)
GPIO.setup(blueRGBPin2,GPIO.OUT)
GPIO.setmode(GPIO.BOARD) # Note This is specifying the physical pins on the Raspberry Pi Header 
GPIO.setwarnings(False)
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(yellow_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
p = GPIO.PWM(3, 50)     # Sets up pin 11 as a PWM pin
p.start(0)               # Starts running PWM on the pin and sets it to 0


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

while True:
 #Move the servo back and forth
    p.ChangeDutyCycle(1)     # Changes the pulse width to 3 (so moves the servo)
    sleep(0.3)                 # Wait 1 second
    p.ChangeDutyCycle(4)    # Changes the pulse width to 12 (so moves the servo)
    sleep(0.3)

# Clean up everything
#p.stop()                 # At the end of the program, stop the PWM
#GPIO.cleanup()           # Resets the GPIO pins back to defaults

# Ask the user which LEDs to turn on or off
while True:
    led_color = input("Enter LED color (red, yellow, green): ")
    led_state = input("Enter state (on or off): ")

    if led_color == "red":
        if led_state == "on":
            print("Red LED On")
            GPIO.output(red_pin,GPIO.HIGH)
        elif led_state == "off":
            print("Red LED Off")
            GPIO.output(red_pin,GPIO.LOW)
        else:
            print("Invalid")
    elif led_color == "yellow":
        if led_state == "on":
            print("Yellow LED On")
            GPIO.output(yellow_pin,GPIO.HIGH)
        elif led_state == "off":
            print("Yellow LED Off")
            GPIO.output(yellow_pin,GPIO.LOW)
        else:
            print("Invalid")
    elif led_color == "green":
        if led_state == "on":
            print("Green LED On")
            GPIO.output(green_pin,GPIO.HIGH)
        elif led_state == "off":
            print("Green LED Off")
            GPIO.output(green_pin,GPIO.LOW)
        else:
            print("Invalid")
        
    else:
        print("Invalid")
    response = input("Do you want to continue?(yes/no): ")
    if response.lower() == "no":
        break
    