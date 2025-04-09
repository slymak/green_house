#!/usr/bin/python3
#pip install w1thermsensor
from datetime import datetime
import time
from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import logging
logging.basicConfig(format='%(asctime)s - %(message)s',filename='/home/sklep/sklenik/logs/actuator')

movetime = 11	#how many sec actuator works

pohyb = 25      # move actuator 10 sec cca 10cm
polarita = 26   # change polarity for actuator -LOW move down

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pohyb, GPIO.OUT)
GPIO.setup(polarita, GPIO.OUT)

dts = datetime.now()
dt  = dts.strftime('%Y-%m-%d %H:%M')


############ using value from logs
stepf = open("/home/sklep/sklenik/logs/step","r")
step = int(stepf.read())
stepf.close()

########### ds1820 temperatur ############################
sensor_data = []
for sensor in W1ThermSensor.get_available_sensors():
  sensor_data.append("%.0f" % (sensor.get_temperature()))


def moveup_window(co):
	print(co)
	#switch ON
	#switch OFF
	GPIO.output(pohyb, GPIO.HIGH)
	GPIO.output(polarita, GPIO.HIGH)

def move_up(stepn):
  f = open("/home/sklep/sklenik/logs/step","w")
  f.write(str(stepn))
  f.close
  logging.warning(f" UP set {stepn}  real t {real_temp}")
  #switch ON
  GPIO.output(pohyb, GPIO.LOW)
  time.sleep(14)
  #switch OFF
  GPIO.output(pohyb, GPIO.HIGH)
  GPIO.output(polarita, GPIO.HIGH)

def move_down(stepn):
	f = open("/home/sklep/sklenik/logs/step","w")
	f.write(str(stepn))
	f.close
	logging.warning(f" down set {stepn}  real t {real_temp}")
	#switch ON
	GPIO.output(pohyb, GPIO.LOW)
	GPIO.output(polarita, GPIO.LOW)
	time.sleep(15)
	#switch OFF
	GPIO.output(pohyb, GPIO.HIGH)
	GPIO.output(polarita, GPIO.HIGH)


real_temp = int(sensor_data[0])
#print(real_temp)
#real_temp = 23

#### 1.st move up
if real_temp > 24 and step == 0:
	move_up(2)
	print(f"1 step up  temp je {real_temp} a pisem 2")

#### 1.st move down
if real_temp < 21 and step == 2:
	move_down(1)
	print(f"1 step down temp je {real_temp} a pisem 1")

#### 2.st move up
if real_temp > 27 and step < 4:
	move_up(4)
	print(f"2 step up temp je {real_temp} a pisem 4")

#### 2.st move down
if real_temp < 23 and step == 4:
	move_down(3)
	print(f"2 step down temp je {real_temp} a pisem 3")

if real_temp < 20 and step > 0:
	move_down(0)
	print(f"last step down temp je {real_temp} a pisem 0")
