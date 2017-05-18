import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
a = [20, 21]
GPIO.setup(a, GPIO.OUT)

while True:
    GPIO.output(a, (GPIO.HIGH, GPIO.LOW))
    time.sleep(1)
    GPIO.output(a, (GPIO.LOW, GPIO.HIGH))
    time.sleep(1)


