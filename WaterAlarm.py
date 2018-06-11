#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 21

GPIO.setup(pin, GPIO.IN)

state = GPIO.input(pin)

print(state)

