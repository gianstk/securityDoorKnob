import picamera
import time

camera = picamera.PiCamera()
camera.vflip = True
camera.capture("example.jpg")