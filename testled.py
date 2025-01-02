import RPi.GPIO as GPIO
import time

# Configuration des pins
red_pin = 11
green_pin = 12
blue_pin = 13

# Setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

colors = [(1,0,0), (0,1,0), (0,0,1)] # Rouge, Vert, Bleu

try:
   while True:
       for r,g,b in colors:
           GPIO.output(red_pin, r)
           GPIO.output(green_pin, g) 
           GPIO.output(blue_pin, b)
           time.sleep(1)

except KeyboardInterrupt:
   GPIO.cleanup()