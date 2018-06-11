#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import Config

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.IN)

state = GPIO.input(pin)

print(state)

