#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

state = GPIO.input(23)

print(state)
pin = 23
state2 = GPIO.gpio_function(pin)
print(state2)
