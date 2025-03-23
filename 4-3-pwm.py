import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

a = GPIO.PWM(24, 1000)
a.start(0)

try:
    while (True):
        print("Enter a number from 0 to 100")
        s = input()
        if s == 'q': break
        try:
            d = float(s)
            print(f"Current voltage is {3.3*d/100.0}")
            a.ChangeDutyCycle(d)
            if (d < 0) or (d > 100):
                print("Your number should be [0..100]")
                continue

            
        except ValueError:
            print('Input is not a number')
finally:
    a.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()
