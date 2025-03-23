import RPi.GPIO as GPIO
import time as t

def decimalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while(True):
        print("Enter period of triangle signal")
        s = input()
        try:
            period = float(s)
            if (period <= 0): 
                print("Number should be above zero")
                continue
            
            dt = period/512.0
            for i in range(256):
                GPIO.output(dac, decimalToBinary(i))
                t.sleep(dt)
            
            for i in range(256):
                GPIO.output(dac, decimalToBinary(255-i))
                t.sleep(dt)
        except ValueError:
            if s == 'q': break

            print("Period should be number")

finally:
    GPIO.output(dac, [0]*len(dac))