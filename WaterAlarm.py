#!/usr/bin/python
# -*- coding: <lolilol> -*-

import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)

pin = 21


GPIO.setup(pin, GPIO.IN)

while waterAlarm == 0: # Tant que i est strictement inférieure à 10

  state = GPIO.input(pin)
  print(state)
  time.sleep(5)
