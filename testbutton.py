import RPi.GPIO as GPIO
import time

button_pin = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
   while True:
       if not GPIO.input(button_pin):
           print("Bouton appuyé!")
           time.sleep(0.2)  # Debouncing
           
except KeyboardInterrupt:
   GPIO.cleanup()