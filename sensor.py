import RPi.GPIO as GPIO
import adafruit_ssd1306
import adafruit_mlx90614
import RPi_I2C_driver
from PIL import Image, ImageDraw, ImageFont
from time import sleep, time
import board
import numpy as np
import threading

# import busio

# assign attribute
USTrigger = 24
USEcho = 23
pin_buzzer = 4
global jarak

GPIO.setup(USTrigger, GPIO.OUT)
GPIO.setup(USEcho, GPIO.IN)
GPIO.setup(pin_buzzer, GPIO.OUT)
i2c = board.I2C()  # i2c for mlx90614
lcd = RPi_I2C_driver.lcd()
mlx = adafruit_mlx90614.MLX90614(i2c)


# sonar.distance() to measure distance
# sudo pip3 install adafruit-circuitpython-hcsr04
# adafruit-circuitpython-ssd1306

# Main program



def welcome_screen():
    lcd.lcd_clear()
    lcd.lcd_display_string("Selamat Datang", 1)

def get_close():
    lcd.lcd_clear()
    lcd.lcd_display_string("Mendekat sekitar",1)
    lcd.lcd_display_string("      20CM",2)

def show_result():
    # draw.text((x + 42, top + 50), str(round(jarak_mean,2)) + " cm", font=font, fill=255)
    # oled.image(image)
    # oled.show()
    return suhu


# MLX90614 initiation
def temp():
    suhu = round(mlx.object_temperature, 2)
    return suhu


# HC-SR04 Initiation
def distance():
    GPIO.output(USTrigger, GPIO.LOW)
    sleep(.01)
    GPIO.output(USTrigger, GPIO.HIGH)

    sleep(0.00001)

    GPIO.output(USTrigger, GPIO.LOW)

    while GPIO.input(USEcho)==0:
          pulse_start_time = time()
    while GPIO.input(USEcho)==1:
          pulse_end_time = time()

    pulse_duration = pulse_end_time - pulse_start_time
    jarak = round(pulse_duration * 17472.5, 2)
    return jarak

# Buzzer Initiation
def buzzer(time, delay):
    for i in range(time):
        GPIO.output(pin_buzzer, GPIO.HIGH)
        sleep(delay)
        GPIO.output(pin_buzzer, GPIO.LOW)
        if i != time:
            sleep(delay)


def main():
    t1 = threading.Thread(target=led_blue, args=(1, 3))
    t1.start()
    welcome_screen()
    sleep(3)
    get_close()
    counter = 1
    arr = [None, None, None, None, None]
    t1.join()
    while not counter == 6:
        jarak = round(distance(), 2)
        if jarak < 25.0:
            arr[counter - 1] = jarak
            counter += 1

    global jarak_mean
    jarak_mean = sum(arr) / len(arr)

    show_result()
    t2=threading.Thread(target=buzzer, args=(1, 2))
    t3=threading.Thread(target=led_blue, args=(4, .5))
    t2.start()
    t3.start()
    sleep(2)
    t2.join()
    t3.join()


# try:
#     while True:
#         main()
# except KeyboardInterrupt:
#     GPIO.cleanup()
#     oled.fill(0)
#     oled.show()
