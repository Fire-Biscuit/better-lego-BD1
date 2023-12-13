import RPi.GPIO as GPIO
from time import sleep

holoprojectorLED = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(holoprojectorLED,GPIO.OUT)

holoprojector = GPIO.PWM(holoprojectorLED, 1000)
holoprojector.start(0)

for i in range(4, 10, 1):
    if (i % 2) == 0:
        holoprojector.ChangeDutyCycle(0)
    else:
        holoprojector.ChangeDutyCycle(100)
        
    sleep(((-0.01*(i*i))+1)/4)
for i in range(0, 101, 10):
    holoprojector.ChangeDutyCycle(i)
    sleep(0.1)
holoprojector.ChangeDutyCycle(100)