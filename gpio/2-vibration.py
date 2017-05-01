import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)
count = 0
try:
    while True:
        if GPIO.input(21) == 1:
            time.sleep(0.01)
            if GPIO.input(21) == 1:
                print("vibration detect! " + str(count))
                count += 1
                time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("exit")





