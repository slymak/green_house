#!/usr/bin/python3
#pip install  adafruit-circuitpython-mcp3xxx
#from datetime import datetime
#dts = datetime.now()
#dt  = dts.strftime('%Y-%m-%d %H:%M')


import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan1 = AnalogIn(mcp, MCP.P0)
chan2 = AnalogIn(mcp, MCP.P1)
chan8 = AnalogIn(mcp, MCP.P7)

while True:
#    print('1 Raw ADC Value: ', chan1.value)
    print('1 ADC Voltage: ' + str(chan1.voltage) + 'V')
#    print('2 Raw ADC Value: ', chan1.value)
    print('2 ADC Voltage: ' + str(chan2.voltage) + 'V')
    print('-------------------')
#    print('8 Raw ADC Value: ', chan8.value)
#    print('8 ADC Voltage: ' + str(chan8.voltage) + 'V')
    time.sleep(4)
