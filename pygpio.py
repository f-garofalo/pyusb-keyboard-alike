#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [24]

# loop through pins and set mode and state to 'high'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeS = 0.5

# main loop

try:

    for i in pinList:
      GPIO.output(i, GPIO.LOW)
      time.sleep(SleepTimeS)

    for i in pinList:
      GPIO.output(i, GPIO.HIGH)
      time.sleep(SleepTimeS)

    pinList.reverse()
    GPIO.cleanup()

# End program cleanly with keyboard
except KeyboardInterrupt:
  print("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()

# find more information on this script at
# http://youtu.be/WpM1aq4B8-A


