from machine import Pin, PWM, I2C, ADC
import ssd1306
import time
from time import sleep
#--- I2C & OLED Setup ---
i2c    = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
oled  = ssd1306.SSD1306_I2C(128, 64, i2c)
light = ADC(Pin(28))
#--- RGB LED Pins ---
red   = PWM(Pin(13))
green = PWM(Pin(14))
blue  = PWM(Pin(15))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

while True:
    light_value = light.read_u16()
    print(light_value)
    oled.text('Light Sensor' , 0, 0)
    oled.text('Light ', 0, 10)
    oled.text(str(light_value), 50, 20)
    oled.show()
    sleep(0.1)
#--- Buzzer Pin --
buzzer = PWM(Pin(12))
buzzer.freq(500)

#--- Color Function ---
def set_color(r, g, b):
    red.duty_u16(int(r / 255 * 65535))
    green.duty_u16(int(g / 255 * 65535))
    blue.duty_u16(int(b / 255 * 65535))

#--- Buzzer Beep ---
def buzzer_beep():
    buzzer.duty_u16(590)
    time.sleep(1)
    buzzer.duty_u16(900)
    buzzer.duty_u16(100)
    

#--- OLED Message Function ---
def show_message(line1="", line2="", line3="", line4=""):
    oled.fill(0)                  # Clear screen
    oled.text(line1, 0,  0)       # Line 1 - top
    oled.text(line2, 0, 16)       # Line 2
    oled.text(line3, 0, 32)       # Line 3
    oled.text(line4, 0, 48)       # Line 4 - bottom
    oled.show()                   # Push to display

#--- Color List ---
colors = [
    ("Dawood",    255,   0,   0),
    ("Dylan",    0, 255,   0),
    ("Daniel",     0,   0, 255),
    ("Dawn", 255, 255,   0),
    ("Ndegeee",     0, 255, 255),
    ("Wanjee", 128,   0, 128),
    ("Leon",  255, 255, 255),
    ("Clement", 255, 165,   0),
]

#--- Startup Message ---
show_message("  PICO PROJECT", "----------------", " LED + BUZZER", "  + OLED READY!")
buzzer_beep()
time.sleep(2)

#--- Main Loop ---
while True:
    for name, r, g, b in colors:
        print(f"Group M: {name}")
        set_color(r, g, b)
        buzzer_beep()
        show_message(
            "ALL BLACKS",
            "----------------",
            f"  Now: {name}",
            "  WEKA  MAWE :)"
        )
        time.sleep(1.5)

    # --- Reset ---
    set_color(0, 0, 0)
    show_message("   ALL DONE!",  "----------------", " Restarting...", "")
    time.sleep(1)