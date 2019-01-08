import RPi.GPIO as GPIO
import time

pin = 2

def main(mode):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)

    p = GPIO.PWM(2, 50)
    p.start(2.5)

    try:
        while True:
            if mode == "open":
                p.ChangeDutyCycle(5.8) #8.7
            elif mode == "close":
                p.ChangeDutyCycle(8.7)
            time.sleep(0.5)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()


def test():
        print("print")
        while True:
                main("close")
                print("close")
                time.sleep(3)
                main("open")
                print("open")
                time.sleep(3)
test();

