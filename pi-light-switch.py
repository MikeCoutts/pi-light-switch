# Copyright The Kavinjka Software Company 2021
#
# Authour MikeC@kavinjka.com

import RPi.GPIO as GPIO
import time # for sleep functions

from signal import signal, SIGINT # for Ctrl-C
from sys import exit
from datetime import datetime

# Initialize the  GPIO Infrastructure to BCM (Broadcom SOC channel)
GPIO.setmode(GPIO.BCM)

# Define the button GPIO port as an Input GPIO Pin and previous_input variable
BUTTON = 16
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 16 (button) to be an input pin and set initial value to be pulled low (off)
previous_input = False

# define the Green LED GPIO port as an Output Pin and light_on variable
GREEN = 26
GPIO.setup(GREEN, GPIO.OUT) 
light_on = False

# Define exit handler for the program (called on Ctrl-C)
def ctrl_c_handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    GPIO.cleanup()
    exit(0)

# setup  the Ctrl-C handler
signal(SIGINT, ctrl_c_handler)

# infinite loop for the main thread (Use Cntrl-C to exit)
while True:
  # take a reading from the switch
  input = GPIO.input(BUTTON)

  # if the last reading was high and this one is low, signal Button Released
  if ((previous_input) and not input):
    currentDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Button Released at", currentDateTime)

    if (light_on == True):
      GPIO.output(GREEN, GPIO.LOW)
      light_on = False
    else:
      GPIO.output(GREEN, GPIO.HIGH)
      light_on = True

  # update prev_input value
  previous_input = input

  # slight pause to debounce
  time.sleep(0.05)
