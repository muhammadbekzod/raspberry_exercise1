import RPi.GPIO as GPIO
import math
import time

pwnPin = 18
ledPin = 23
butPin = 17

duty =0

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwnPin, GPIO.OUT)
GPIO.setup(butPin,GPIO.IN, pull_up_down=GPIO.PUD_UP)
pwm=GPIO.PM(pwnPin, 200)

GPIO.output(ledPin,GPIO.LOW)
pwm.start(duty)


def mapFun(x, inLo, inHi, outLo, outHi):
    inRange = inHi - inLo
    outRange = outHi - outLo
    inScale = (x - inLo) / inRange 
    return outLo + (inScale * outRange)

x=0

try:
    while 1:
        if GPIO.input(butPin):
            step = 0.1
        else:
            step = 0.3

        duty = mapFun(math.sin(x), -1,1,0,100)
        x += step
        pwm.ChangeDutyCycle(duty)
        time.sleep(0.05)

except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
