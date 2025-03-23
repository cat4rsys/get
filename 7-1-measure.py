import RPi.GPIO as GPIO
import time as t
import matplotlib.pyplot as plt

def decimalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def sar():
    value = 128

    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 128
    
    value += 64
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 64
    
    value += 32
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 32
    
    value += 16
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 16
    
    value += 8
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 8
    
    value += 4
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 4
    
    value += 2
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 2
    
    value += 1
    GPIO.output(dac, [int(bit) for bit in bin(value)[2:].zfill(8)])
    t.sleep(0.005)
    if GPIO.input(comp): 
        value -= 1
    
    return value

def numInLed(value):
    binNum = decimalToBinary(value)
    GPIO.output(led, binNum)
    return binNum

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
led    = [2, 3, 4, 17, 27, 22, 10, 9]
comp   = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

voltage = []

maxVoltage = 3.3
maxLevel = 255

try:
    curLevelOfVoltage = 0
    GPIO.output(troyka, 1)
    timeOfStart = t.time()

    chargingUntilLevel = 211
    unchargingUntilLevel = 176

    while(curLevelOfVoltage < chargingUntilLevel):
        curLevelOfVoltage = sar()
        numInLed(curLevelOfVoltage)
        voltage.append(3.3 * curLevelOfVoltage / maxLevel)

    GPIO.output(troyka, 0)

    while(curLevelOfVoltage > unchargingUntilLevel):
        curLevelOfVoltage = sar()
        numInLed(curLevelOfVoltage)
        voltage.append(3.3 * curLevelOfVoltage / maxLevel)

    timeOfEnd = t.time()
    period = (timeOfEnd - timeOfStart) / len(voltage)
    with open("settings.txt", "w") as f:
        f.write(str(period))
        f.write("\n")
        f.write(str(maxVoltage / 256))

    print("time:", timeOfEnd - timeOfStart, "period:", period, "freq:", 1.0 / period, "delta Level:", maxVoltage / 256)

    with open("data.txt", "w") as f:
        for i in range(len(voltage)):
            f.write(str(voltage[i]))
            f.write("\n")

    plt.plot(range(len(voltage)), voltage)
    plt.show()
finally:
    GPIO.output(dac, [0]*8)
    GPIO.output(led, [0]*8)
    GPIO.cleanup()