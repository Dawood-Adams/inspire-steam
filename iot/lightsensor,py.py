# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-analog-inputs-micropython/
from machine import Pin, ADC
from time import sleep

light = ADC(Pin(28))

while True:
  light_value = light.read_u16() # read value, 0-65535 across voltage range 0.0v - 3.3v
  print(light_value)
  sleep(0.1)