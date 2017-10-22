#!/usr/bin/env python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)

while True:
  input = GPIO.input(21)
  if not input:
    print("RESET!!")
    os.system("reboot")
  time.sleep(1)
