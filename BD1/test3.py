from random import randint
import os
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

holoprojector = 23
eye = 16

GPIO.setup(holoprojector,GPIO.OUT)
GPIO.setup(eye,GPIO.OUT)

GPIO.output(holoprojector,GPIO.LOW)
GPIO.output(eye,GPIO.LOW)

files = ["confused1",\
        #0
        "happy1","happy2","happy3","happy4",\
        #1        2        3        4
        "mean1","mean2",\
        #5       6
        "mechanism1","mechanism2",\
        #7            8
        "music1","music2","music3","music4",\
        #9        10       11       12
        "system1","system2","system3","system4",\
        #13        14        15        16
        "system5","system6","system7",\
        #17        18        19
        "talking1","talking2","talking3","Talking4",\
        #20         21         22         23
        "talking5","talking6","talking8",\
        #24         25         26
        "talking9","talking10","talking11",\
        #27         28          29
        ]
        
print(len(files))

while True:
    fileNumber = randint(0,len(files)-1)
    print(fileNumber)
    file = files[fileNumber]
    print(file)
    GPIO.output(holoprojector,GPIO.HIGH)
    GPIO.output(eye,GPIO.HIGH)
    os.system("mpg123 " + "BD1Sounds/" + file + ".mp3")
    GPIO.output(holoprojector,GPIO.LOW)
    GPIO.output(eye,GPIO.LOW)
    sleep(1)