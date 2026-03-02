# Name : Dawood Adams
# Date : 26/02/2026
# program to blink leds
import machine
from machine import Pin
import time

red_led = Pin(28, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
while True:
    red_led.on()                 # set pin to "on" (high) level
    yellow_led.off()
    time.sleep(0.2) # Wait for USB to become ready
    print("heya")
    red_led.off()
    yellow_led.on()
    time.sleep(0.5) 
    print("Learning the basics")