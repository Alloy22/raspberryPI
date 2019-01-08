import RPi.GPIO as GPIO
import pwm as drive
import keyinput as key
import tapesensor as ts
import sMotor as grip
import time



def main():
        driving()
        grip.main("close")

        drive.spinLeft()
        time.sleep(5)
        drive.allStop()

def driving():
    while True:
      leftSensor = ts.irsensorL()
      rightSensor = ts.irsensorR()

      if leftSensor == "white" and rightSensor == "black":
                drive.spinRight()
      elif leftSensor == "black" and rightSensor == "white":
                drive.spinLeft()
      elif leftSensor == "white" and rightSensor == "white":
                drive.allStop()
                #break;
      else:
                drive.forwardDrive()
      time.sleep(0.01)
      print(leftSensor + "hi" + rightSensor)

def wasd():
        while True:
                hi = key.readkey()
                if hi:
                        print(hi)

driving()
