#
import RPi.GPIO as GPIO
import time


# Assign GPIO pins for each LED color
red_pin = 29
yellow_pin = 31
green_pin = 37
GPIO.setmode(GPIO.BOARD) # Note This is specifying the physical pins on the Raspberry Pi Header 
GPIO.setwarnings(False)
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(yellow_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)

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
        
