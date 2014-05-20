#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
if not os.getuid() == 0:
    sys.exit('Needs to be root for running this script.')
import RPi.GPIO as GPIO
import time
# the stop signal
BTN_IO = 12
# we use the board numbering of the I/O
# ie the RasPi header pin numbering
GPIO.setmode(GPIO.BOARD)
# the I/O is configured as input with pullup enabled
GPIO.setup(BTN_IO, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.HIGH)
def stopFunction(channel):
  os.system("sudo halt")
GPIO.add_event_detect(BTN_IO, GPIO.RISING, callback = stopFunction, bouncetime = 300)
try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  GPIO.cleanup()
GPIO.cleanup()
