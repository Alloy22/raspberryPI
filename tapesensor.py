import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

IRPINL = 7 #8 assumes you've connected the IR Out wire to GPIO4
IRPINR = 8

def irsensorL(): #function to get value from IR sensor
    pulse_end = 0
    GPIO.setup(IRPINL, GPIO.OUT) #Set your chosen pin to an output
    GPIO.output(IRPINL, GPIO.HIGH) #turn on the power 5v to the sensor
    time.sleep(0.01) #charge the tiny capacitor on the sensor for 0.1sec
    pulse_start = time.time() #start the stopwatch
    GPIO.setup(IRPINL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to pull down to ground 0v
    while GPIO.input(IRPINL)> 0:
        pass #wait while the capacitor discharges to zero
    if  GPIO.input(IRPINL)==0:
        pulse_end = time.time() #when it hits zero stop the stopwatch
    pulse_duration = pulse_end - pulse_start
    print "duration:", pulse_duration #print the time so you can adjust sensitivity
    if pulse_duration > 0.00042 and pulse_duration < 0.001: #adjust this value to change the sensitivity
        colour_seen = "black"
    else:
        colour_seen = "white"
    return colour_seen

def irsensorR(): #function to get value from IR sensor
        pulse_end = 0
        GPIO.setup(IRPINR, GPIO.OUT) #Set your chosen pin to an output
        GPIO.output(IRPINR, GPIO.HIGH) #turn on the power 5v to the sensor
        time.sleep(0.01) #charge the tiny capacitor on the sensor for 0.1sec
        pulse_start = time.time() #start the stopwatch
        GPIO.setup(IRPINR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # set pin to pull down to ground 0v
        while GPIO.input(IRPINR)> 0:
            pass #wait while the capacitor discharges to zero
        if  GPIO.input(IRPINR)==0:
            pulse_end = time.time() #when it hits zero stop the stopwatch
        pulse_duration = pulse_end - pulse_start
        print "duration:", pulse_duration #print the time so you can adjust sensitivity
        if pulse_duration > 0.00042 and pulse_duration < 0.001: #adjust this value to change the sensitivity
            colour_seen = "black"
        else:
            colour_seen = "white"
        return colour_seen

def main():
    while(1):
        irsensorL()
        time.sleep(0.2)


   #GPIO.cleanup() #always good practice to clean-up the GPIO settings at the end :) tobyonlineq
