from machine import Pin, I2C, ADC

import framebuf
import utime
#from my_dht import DHTSensor  # GP22 sensor
import machine
import time
#import urequests
#import network
#import ujson
#import dht
#from machine import Speaker
buzzerPin = 13

buzzer = Pin(buzzerPin, Pin.OUT)

while True:
    buzzer.value(1)
    time.sleep(0.2)
    buzzer.value(0)
    time.sleep(0.2)

# Function to read room temperature and humidity
#def read_room_temperature_humidity():
 #   dht_sensor.measure()
  #  temperature = dht_sensor.temperature()
   # humidity = dht_sensor.humidity()
    #return temperature, humidity

# Function to send data to ThingSpeak

#def sound_alarm():
 #   speaker.on()
  #  sleep(1)
   # speaker.off()
    #sleep(1)

# OLED resolution
#pix_res_x = 128
#pix_res_y = 64

# ----- DHT22 Setup -----
#sensor = DHTSensor(26)  # GP22


#

# Display logo once at startup

#while True:
   