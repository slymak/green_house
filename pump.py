#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

<<<<<<< HEAD
pump = 23	# pumpa
=======
pump = 23       # pumpa
>>>>>>> 1198eccf4072a2b1a9d4760e2357ef813d703c24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pump, GPIO.OUT)

#switch ON
GPIO.output(pump, GPIO.LOW)
time.sleep(13)

#switch OFF 
GPIO.output(pump, GPIO.HIGH)

#GPIO.cleanup()
