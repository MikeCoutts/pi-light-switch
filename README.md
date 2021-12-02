# pi-light-switch
A simple Raspberry PI Python program to show the integration between a momentary push switch and an LED

Read the status of a momentary switch on GPIO Pin 16 (note the use of a Blue LED in place of a 10k Ohm Pull down resistor)

On detection of the trailing edge (as the switch is released) output "Button Released" and the Current DATETIME
Based on a state variable turn a single Green LED on/Off as appropriate

![Alt text](https://github.com/MikeCoutts/pi-light-switch/blob/main/images/IMG_20211103_225959778.jpg?raw=true "Traffic Lights")

# Simple Raspberry Pi Bread Board wiring for this project
[Buzzer](https://www.amazon.com/dp/B07S85WRSZ?psc=1&ref=ppx_yo2_dt_b_product_details) ground on 5V GND line with +ve into GPIO 23.

[Multi Color LED] Blue (GPIO 17), Green (GPIO 23) and Red (GPIO 22) connected to BGR Anodes via 10K Ohm Resitors with Cathode to Ground.

[Individual LED's] Red (GPIO 13), Amber/Yellow (GPIO 19), Green (GPIO 26) connected to Red/Amber/Green Anodes via 10K Ohm resitors.

10K Ohm resiter supplying power to momentary switch with a Blue line (connected to GPIO Input 16) being drawn down by the Blue LED.

# Operation of the Program
import RPi.GPIO, time, signal.signal, signal.SIGINT, sys.exit and datetime.datetime

Define the button Input as GPIO Pin 16 and a previous_state variable
Define the Green LED output as GPIO Pin 26 and define a light_on variable

Define the exit handler as we will be using an infinete loop

Enter an infinite loop (while True:) where we grab the state of the switch using input = GPIO.input(button)

  Upon Button depression the Blue LED get's a simple direct power supply (via a 10K Ohm resister) with the side effect of bringing the "Button" Line Low (input = True)

  Upon release the program detects the rising edge (input = False) gets the currentDateTime and prints out a message to the console
  Based on the value of light_on turn the Green LED On/Off as appropriate

  On each loop update previous_input with the current input value and have a slight pause just to debounce the button press (code runs way faster than buttons)
