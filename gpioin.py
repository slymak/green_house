#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

pin16 = 16
pin20 = 20
pin21 = 21

GPIO.setmode(GPIO.BCM)
#GPIO.setup(pin16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  # or this is for waterlevel
GPIO.setup(pin16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(pin20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(pin16):
    print('Input16 was HIGH')
else:
    print('Input16 was LOW')

if GPIO.input(pin20):
    print('Input20 was HIGH')
else:
    print('Input20 was LOW')
