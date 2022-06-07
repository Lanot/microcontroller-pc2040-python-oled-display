#See: https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py
import machine
import time
from ssd1306 import SSD1306_I2C
import framebuf

# OLED pixel definition (WxH)
WIDTH  = 128
HEIGHT = 64

# I2C0 pin assignments
SCL = 5
SDA = 4

imageBuffer = bytearray(b"\x00\x00\x00\x00\x7F\x80\x01\x98\x7F\x80\x03\xFC\x60\x60\x03\x6C\x60\x60\x03\xFC\x60\x18\x03\xFC\x60\x18\x01\x98\x60\x60\x00\xF0\x60\x60\x00\x60\x7F\x80\x00\x00\x7F\x80\x00\x00\x60\x00\x00\x00\x66\x3C\x0F\x00\x66\x7F\x3F\xC0\x60\x63\x30\xC0\x66\x60\x20\x40\x66\x60\x20\x40\x66\x60\x20\x40\x66\x63\x30\xC0\x66\x7F\x3F\xC0\x06\x3C\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x3F\xFF\xFF\xF8\x00\x00\x00\x00\x15\x55\x55\x50\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

#Initialize the onboard LED as output
led = machine.Pin(25, machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    led.toggle()

# Initialize I2C0, Scan and Debug print of SSD1306 I2C device address
i2c = machine.I2C(0, scl=machine.Pin(SCL), sda=machine.Pin(SDA), freq=200000)
print("Device Address      : "+hex(i2c.scan()[0]).upper())

# Initialize OLED
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Initialize timer_one. Used for toggling the on board LED
timer_one = machine.Timer()

# Timer one initialization for on board blinking LED at 200mS interval
timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)

i = 0
while True:
    T, H = 22, 56
    display.fill(0)

    # # Write the Temperature and Humidity ICON
    fb = framebuf.FrameBuffer(imageBuffer, 32, 32, framebuf.MONO_HLSB)
    display.blit(fb, 0, 0)

    display.text('Iteration #: ' + str(i), 0, 40, 2)
    display.show()
    i += 1

    # Wait for Five seconds. Then proceed to collect next sensor reading.
    time.sleep_ms(5000)

# from machine import Pin, I2C
# import sh1106
# import sys
# import utime
#
# # OLED pixel definition (WxH)
# WIDTH  = 128
# HEIGHT = 64
#
# # I2C0 pin assignments
# SCL = 5
# SDA = 4
#
# sys.stdout.write('\nINIT #1')
#
# sys.stdout.write('\nINIT #2')
# i2c = I2C(0, scl=(SCL), sda=Pin(SDA))
#
# sys.stdout.write('\nINIT #3')
# display = sh1106.SH1106_I2C(WIDTH, HEIGHT, i2c, None, 0x3c)
# display.sleep(False)
# sys.stdout.write('\nINIT #4')
#
# i = 0
# while True:
#     sys.stdout.write('\ni: ' + str(i))
#
#     display.fill(0)
#     display.text('CoderDojo: ' + str(i), 0, 0, 1)
#     display.show()
#     i += 1
#
#     utime.sleep_ms(1000)
