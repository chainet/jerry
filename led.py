import RPi.GPIO as GPIO
import time

GPIO.cleanup()
#BOARD编号方式, 基于插座引脚编号
GPIO.setmode(GPIO.BOARD)
RedLight = 11
YellowLight = 13
GreenLight = 12
#输出模式
GPIO.setup(GreenLight, GPIO.OUT)
GPIO.setup(RedLight, GPIO.OUT)
GPIO.setup(YellowLight, GPIO.OUT)

while True:
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(GreenLight, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(YellowLight, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(YellowLight, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(RedLight, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(RedLight, GPIO.LOW)
    time.sleep(0.3)