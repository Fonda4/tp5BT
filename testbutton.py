from machine import Pin
import time

button = Pin(16, Pin.IN, Pin.PULL_UP)

while True:
   if not button.value():
       print("Bouton appuyé!")
       time.sleep(0.2)