from gpiozero import PWMOutputDevice
from gpiozero import DigitalOutputDevice
from time import sleep
import RPi.GPIO as GPIO

PWM_DRIVE_LEFT = 21
FORWARD_LEFT_PIN = 17
REVERSE_LEFT_PIN = 22


PWM_DRIVE_RIGHT = 5
FORWARD_RIGHT_PIN = 23
REVERSE_RIGHT_PIN = 24

driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT, True, 0, 1000)
driveRight = PWMOutputDevice(PWM_DRIVE_RIGHT, True, 0, 1000)

forwardLeft = PWMOutputDevice(FORWARD_LEFT_PIN)
reverseLeft = PWMOutputDevice(REVERSE_LEFT_PIN)
forwardRight = PWMOutputDevice(FORWARD_RIGHT_PIN)
reverseRight = PWMOutputDevice(REVERSE_RIGHT_PIN)

high = 0.4
medium = 0.4
low = 0.2

mod = 0.03

FRspeed = 1 #0.26 - mod
FRspeedL = 1 #0.27 - mod
Sspeed = 1 #0.53

def allStop():
        forwardLeft.value = False
        reverseLeft.value = False
        forwardRight.value = False
        reverseRight.value = False
        driveLeft.value = 0
        driveRight.value = 0
def forwardDrive():
        forwardLeft.value = True
        reverseLeft.value = False
        forwardRight.value = True
        reverseRight.value = False
        driveLeft.value = FRspeedL
        driveRight.value = FRspeed
def reverseDrive():
        forwardLeft.value = False
        reverseLeft.value = True
        forwardRight.value = False
        reverseRight.value = True
        driveLeft.value = FRspeed
        driveRight.value = FRspeed
def spinLeft():
        forwardLeft.value = False
        reverseLeft.value = True
        forwardRight.value = True
        reverseRight.value = False
        driveLeft.value = Sspeed
        driveRight.value = Sspeed
def spinRight():
        forwardLeft.value = True
        reverseLeft.value = False
        forwardRight.value = False
        reverseRight.value = True
        driveLeft.value = Sspeed
        driveRight.value = Sspeed
def forwardTurnLeft():
        forwardLeft.value = True
        reverseLeft.value = False
        forwardRight.value = True
        reverseRight.value = False
        driveLeft.value = 0
        driveRight.value = Sspeed
def forwardTurnRight():
        forwardLeft.value = True
        reverseLeft.value = False
        forwardRight.value = True
        reverseRight.value = False
        driveLeft.value = Sspeed
        driveRight.value = 0
def reverseTurnLeft():
        forwardLeft.value = False
        reverseLeft.value = True
        forwardRight.value = False
        reverseRight.value = True
        driveLeft.value = low
        driveRight.value = medium
def reverseTurnRight():
        forwardLeft.value = False
        reverseLeft.value = True
        forwardRight.value = False
        reverseRight.value = True
        driveLeft.value = medium
        driveRight.value = low

def main():
        print("f")
        forwardDrive()
        sleep(3)
        print("r")
        reverseDrive()
        sleep(3)
        print("l")
        spinLeft()
        sleep(3)
        allStop()

main()
