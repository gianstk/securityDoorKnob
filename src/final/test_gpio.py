import RPi.GPIO as GPIO
import time

GPIO.cleanup

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

GPIO.output(4, 1)

