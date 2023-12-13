import os
from os import listdir
print("...")

mp3_files = [ f for f in listdir('.') if f[-4:] == '.mp3' ]

if not len(mp3_files) > 0:
    print("No mp3 files found!")
elif len(mp3_files) > 0:
    print("mp3 files found!")
print(mp3_files)
os.system('BDtestOne.mp3 &')