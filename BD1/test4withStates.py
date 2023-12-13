from random import randint
import os
from time import sleep
import RPi.GPIO as GPIO
from threading import Thread

holoprojectorLED = 18
eyeLED = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(holoprojectorLED,GPIO.OUT)
GPIO.setup(eyeLED,GPIO.OUT)

holoprojector = GPIO.PWM(holoprojectorLED, 1000)
holoprojector.start(0)
eye = GPIO.PWM(eyeLED, 1000)
eye.start(0)

files = ["confused1",\
        #0
        "happy1","happy2","happy3","happy4", "happy5", "happy6", "happy7",\
        #1        2        3        4         5         6         7
        "mean1","mean2",\
        #8       9
        "mechanism1","mechanism2",\
        #10           11
        "music1","music2","music3","music4",\
        #12       13       14       15
        "system1","system2","system3","system4",\
        #16        17        18        19
        "system5","system6","system7", "system8", "system9",\
        #20        21        22         23         24
        "talking1","talking2","talking3","Talking4",\
        #25         26         27         28
        "talking5","talking6","talking7","talking8",\
        #29         30         31         32
        "talking9","talking10","talking11", "talking12", "talking13",\
        #33         34          35          36            37
        "happyJump1", "happyTrill1"
        #38            #39
        ]
        
print(len(files))

fileNumbers = [0,0,0,0,0,0,0,0,0]

startingProcesEye = False
endingProcessEye = False
startingProcesHolo = False
endingProcessHolo = False

def normalEye():
    active = False
    while True:
        global startingProcesEye
        global endingProcessEye

        if startingProcesEye == True:
            for i in range(5, 101, 1):
                if i > 5:
                    eye.ChangeDutyCycle(i)
                eye.ChangeDutyCycle(i)
                sleep(0.01)
            startingProcesEye = False
            sleep(1)
            active = True
        
        if active == True:
            number = randint(1,15)
            if number == 1:
                eye.ChangeDutyCycle(0)
                sleep(0.05)
                eye.ChangeDutyCycle(100)
            elif number == 2:
                eye.ChangeDutyCycle(0)
                sleep(0.05)
                eye.ChangeDutyCycle(100)
                eye.ChangeDutyCycle(0)
                sleep(0.05)
                eye.ChangeDutyCycle(100)
            else:
                sleep(0.5)

        if endingProcessEye == True:
            active = False
            for i in range(100, 5, -1):
                if i > 2:
                    eye.ChangeDutyCycle(i)
                sleep(0.01)
            endingProcessEye = False

def holoEye():
    while True:
        global startingProcesHolo
        global endingProcessHolo

        if startingProcesHolo == True:
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
            startingProcesHolo = False

        if endingProcessHolo == True:
            print("off")
            for i in range(100, -1, -5):
                holoprojector.ChangeDutyCycle(i)
                sleep(0.1)
            endingProcessHolo = False


def main():
    while True:

        global startingProcesEye
        startingProcesEye = True
        
        global startingProcesHolo
        startingProcesHolo = True

        sleep(1)

        numberOfFiles = randint(1,4) + 1
        moreFilesAllowed = True
        while moreFilesAllowed == True:
            if numberOfFiles >= 7:
                moreFilesAllowed = False
            ContiniueOrNot = randint(0,1)
            if ContiniueOrNot ==0:
                numberOfFiles += 1
            else:
                moreFilesAllowed = False

        for i in range(0, numberOfFiles, 1):
            fileNumbers[i] = randint(0,len(files)-1)
        print(fileNumbers)
        for i in range(0,numberOfFiles,1):
            file = files[fileNumbers[i]]
            print(file)
            os.system("mpg123 " + "BD1Sounds/" + file + ".mp3")
        
        global endingProcessEye
        endingProcessEye = True

        global endingProcessHolo
        endingProcessHolo = True

        timeToSleep = randint(2, 6)
        print("--------------------->>>>sleeping for :")
        print(timeToSleep)
        print("------------------------------------")
        sleep(timeToSleep)

mainThread = Thread(target=main)
mainThread.start()

normalEyeThread = Thread(target=normalEye)
normalEyeThread.start()

holoEyeThread = Thread(target=holoEye)
holoEyeThread.start()