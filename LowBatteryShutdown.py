# LowBatteryShutdown.py
# Rev 03232018
# This code is complete and can be implemented as it is to safely shutdown
# a Rasbperry Pi using the safe shut down feature on Juice Box Zero.
# This is all Raspberry Pi 101, so it is definitely all open source. Feel
# free to mix, copy, paste, change, etc.
# There is also no warranty provided of any kind with this code.

import os
import RPi.GPIO as GPIO

# This is going to let us use the BCM pin numbers.  The number on JuiceBox
# Zero is labeled
# according to BCM.  See https://pinout.xyz/ for more details on pinouts.

GPIO.setmode(GPIO.BCM)

# This is where you would change the GPIO from pin 16 to 25, if you needed
# to do so on the
# Juice Box Zero board itself. Default is GPIO 16. In order to change the
# hardware, you would
# need to cut the GPIO 16 trace on the board and make a solder bridge over
# GPIO 25.
# See http://www.blog.juiceboxzero.com/ for more details.
shutdown_pin = 16  # defines pin 16 as the pin we're watching
GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def shutdown_callback_function( shutdown_pin ):

    # uncomment the following line to have the Pi tell you that the pin is
    # HIGH and that the callback function has been entered. This is mostly
    # useful for debugging.
    #print("the low battery pin is HIGH now, shutting down.")
    
    os.system("sudo shutdown -h now")

# This is the magic line that adds pin 16 so it is always being watched.
GPIO.add_event_detect(shutdown_pin, GPIO.RISING, callback=shutdown_callback_function)
