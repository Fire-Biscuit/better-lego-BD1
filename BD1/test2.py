from random import randint
import os

files = ["confusedOne",\
         #0
         
        "defaultOne", "defaultTwo", "defaultThree", "defaultFour", "defaultFive", \
        #1 2 3 4 5

        "funnyOne", "funnyTwo", \
        #6 7

        "grumpyOne", "grumpyTwo", \
        #8 9

        "happyOne", "happyTwo", "happyThree", \
        #10 11 12

        "musicOne", "musicTwo", "musicThree", "musicFour", \
        #13 14 15 16

        "scaredOne", "scaredTwo", \
        #17 18

        "talkingOne", "talkingTwo", "talkingThree", "talkingFour", "talkingFive", \
        #19 20 21 22 23

        "weirdOne", "weirdTwo", \
        #24 25

        "workingOne"]
        #26
print(len(files))
fileNumber = randint(0,len(files)-1)
print(fileNumber)
file = files[fileNumber]
print(file)

os.system("mpg123 " + "bdmp3Files/" + file + ".mp3")
