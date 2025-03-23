import RPi.GPIO as GPIO
import time as t

def decimalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def sar():
    value = 128

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 128
    
    value += 64
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 64
    
    value += 32
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 32
    
    value += 16
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 16
    
    value += 8
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 8
    
    value += 4
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 4
    
    value += 2
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 2
    
    value += 1
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.01)
    if GPIO.input(comp): 
        value -= 1
    
    
    return value

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
led    = [2, 3, 4, 17, 27, 22, 10, 9]
comp   = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while (True):
        digitalNum = sar() + 1
        GPIO.output(led, ([0]* (8-digitalNum // 32) + [1] * (digitalNum // 32)))
        
finally:
    GPIO.output(dac, [0]*8)
    GPIO.output(led, [0]*8)
    GPIO.cleanup()