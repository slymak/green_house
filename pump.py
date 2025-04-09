#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

pump = 23	# pumpa

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump, GPIO.OUT)

#switch ON
GPIO.output(pump, GPIO.LOW)
time.sleep(13)

#switch OFF 
GPIO.output(pump, GPIO.HIGH)

#GPIO.cleanup()
