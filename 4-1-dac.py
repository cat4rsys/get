import RPi.GPIO as GPIO

def decimalToBinary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while (True):
        print("Enter a number from 0 to 255")
        s = input()
        if s == 'q': break
        try:
            n = int(s)

            if (n < 0) or (n > 255):
                print("Your number should be [0..255]")
                continue

            print(f"voltage is {float(n)*3.3/256.0}")
            GPIO.output(dac, decimalToBinary(n))
        except ValueError:
            try:
                n = float(s)
                print("You should print integer value")
            except ValueError:
                print('Input is not a number')
finally:
    GPIO.output(dac, [0]*len(dac))
        


