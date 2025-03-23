import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

while True:
    print(GPIO.input(20))
    if (GPIO.input(20)):
        GPIO.output(21, 1)
    else:
        GPIO.output(21, 0)