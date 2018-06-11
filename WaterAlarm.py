#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

state = GPIO.input(21)

print(state)
pin = 21
state2 = GPIO.gpio_function(pin)
print(state2)
