#!/usr/bin/python3
#sudo pip3 install adafruit-blinka
#sudo pip3 install adafruit-circuitpython-mcp3xxx

# SPDX-FileCopyrightText: 2019 Mikey Sklar for Adafruit Industries
# SPDX-License-Identifier: MIT

import os
import time
import datetime
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D22)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan0 = AnalogIn(mcp, MCP.P0)
chan1 = AnalogIn(mcp, MCP.P1)
chan2 = AnalogIn(mcp, MCP.P2)
chan3 = AnalogIn(mcp, MCP.P3)
chan4 = AnalogIn(mcp, MCP.P4)
chan5 = AnalogIn(mcp, MCP.P5)
chan6 = AnalogIn(mcp, MCP.P6)

#print('Raw ADC Value: ', chan0.value)
#print('ADC Voltage: ' + str(chan0.voltage) + 'V')

last_read = 0       # this keeps track of the last potentiometer value
tolerance = 250     # to keep from being jittery we'll only change
                    # volume when the pot has moved a significant amount
                    # on a 16-bit ADC

def remap_range(value, left_min, left_max, right_min, right_max):
    # this remaps a value from original (left) range to new (right) range
    # Figure out how 'wide' each range is
    left_span = left_max - left_min
    right_span = right_max - right_min

    # Convert the left range into a 0-1 range (int)
    valueScaled = int(value - left_min) / int(left_span)

    # Convert the 0-1 range into a value in the right range.
    return int(right_min + (valueScaled * right_span))


tlakomer = remap_range(chan0.value, 0, 65535, 0, 100)
stul2nozka = remap_range(chan1.value, 0, 65535, 0, 100)
stulred = remap_range(chan2.value, 0, 65535, 0, 100)
kabelred = remap_range(chan3.value, 0, 65535, 0, 100)
kabelblue = remap_range(chan4.value, 0, 65535, 0, 100)
kabelbig = remap_range(chan5.value, 0, 65535, 0, 100)
kabel2nozka = remap_range(chan6.value, 0, 65535, 0, 100)

# set OS volume playback volume
#print('Volume = {volume}%' .format(volume = set_volume))
dt = datetime.datetime.now()
datum = dt.strftime("%Y-%m-%d %H:%M")

print(f"{datum} {tlakomer} {stul2nozka} {stulred} {kabelbig} {kabel2nozka} {kabelred} {kabelblue}")
#print(kabelblue)

