#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

pohyb = 25	# pousti actuator 10 sec cca 10cm
polarita = 26	# okna meni smer -LOW zavira

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pohyb, GPIO.OUT)
GPIO.setup(polarita, GPIO.OUT)

#switch ON
GPIO.output(pohyb, GPIO.LOW)
GPIO.output(polarita, GPIO.LOW)
time.sleep(8)

#switch OFF 
GPIO.output(pohyb, GPIO.HIGH)
GPIO.output(polarita, GPIO.HIGH)

#GPIO.cleanup()
