import RPi.GPIO as GPIO
import time as t

def decimalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, decimalToBinary(i))
        t.sleep(0.01)
        if GPIO.input(comp): 
            return i
    return 0

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
comp   = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while (True):
        digitalNum = adc()
        print(f"Digital Number is {digitalNum} Voltage is {digitalNum*3.3/256.0:.2f} V")
finally:
    GPIO.output(dac, [0]*8)
    GPIO.cleanup()