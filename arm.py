import os
import time



os.system("pip3 install keyboard")
import keyboard
while True:
    if keyboard.is_pressed('space'):
        print("Keyboard library works")
        break

os.system("pip install pyfirmata")
from pyfirmata import SERVO, util, Arduino
board = Arduino('COM5')
board.digital[10].mode = SERVO
board.digital[5].mode = SERVO
board.digital[6].mode = SERVO
board.digital[7].mode = SERVO
board.digital[9].mode = SERVO
board.digital[8].mode = SERVO
gripperpin = 10
gripperangle = 0
waistpin = 5
waistangle = 0
shoulderpin = 6
shoulderangle = 0
elbowpin = 7
elbowangle = 0
wristPpin = 9
wristPangle = 0
wristRpin = 8
wristRangle = 0


def opengripper(gripperpin, gripperangle):
    if gripperangle <= 180:
        board.digital[gripperpin].write(gripperangle)
        time.sleep(0.01)

def closegripper(gripperpin, gripperangle):
    if gripperangle >= 0:
        board.digital[gripperpin].write(gripperangle)
        time.sleep(0.01)

def waistleft(waistpin, waistangle):
    if waistangle <= 180:
        board.digital[waistpin].write(waistangle)
        time.sleep(0.01)

def waistright(waistpin, waistangle):
    if waistangle >= 0:
        board.digital[waistpin].write(waistangle)
        time.sleep(0.01)

def shoulderforward(shoulderpin, shoulderangle):
    if shoulderangle <= 140:
        board.digital[shoulderpin].write(shoulderangle)
        time.sleep(0.01)

def shoulderback(shoulderpin, shoulderangle):
    if shoulderangle >= 0:
        board.digital[shoulderpin].write(shoulderangle)
        time.sleep(0.01)

def elbowforward(elbowpin, elbowangle):
    if elbowangle <= 180:
        board.digital[elbowpin].write(elbowangle)
        time.sleep(0.01)

def elbowback(elbowpin, elbowangle):
    if elbowangle >= 0:
        board.digital[elbowpin].write(elbowangle)
        time.sleep(0.01)

def wristup(wristPpin, wristPangle):
    if wristPangle <= 180:
        board.digital[wristPpin].write(wristPangle)
        time.sleep(0.01)

def wristdown(wristPpin, wristPangle):
    if wristPangle >= 0:
        board.digital[wristPpin].write(wristPangle)
        time.sleep(0.01)

def wristleft(wristRpin, wristRangle):
    if wristRangle <= 180:
        board.digital[wristRpin].write(wristRangle)
        time.sleep(0.01)

def wristright(wristRpin, wristRangle):
    if wristRangle >= 0:
        board.digital[wristRpin].write(wristRangle)
        time.sleep(0.01)


while True:

    if keyboard.is_pressed('space'):
        board.digital[13].write(1)
        time.sleep(0.1)
    else:
        board.digital[13].write(0)
        time.sleep(0.1)
    while keyboard.is_pressed('o'):
        for i in range(gripperangle, 180):
            opengripper(gripperpin, i)
            gripperangle = i
            print(gripperangle)
            if keyboard.is_pressed('o') == False:
                break
    while keyboard.is_pressed('c'):
        for i in range(gripperangle, 0, -1):
            closegripper(gripperpin, i)
            gripperangle = i
            print(gripperangle)
            if keyboard.is_pressed('c') == False:
                break
    while keyboard.is_pressed('d'):
        for i in range(waistangle, 180):
            waistleft(waistpin, i)
            waistangle = i
            print(waistangle)
            if keyboard.is_pressed('d') == False:
                break
    while keyboard.is_pressed('a'):
        for i in range(waistangle, 0, -1):
            waistright(waistpin, i)
            waistangle = i
            print(waistangle)
            if keyboard.is_pressed('a') == False:
                break
    while keyboard.is_pressed('w'):
        for i in range(shoulderangle, 140):
            shoulderforward(shoulderpin, i)
            shoulderangle = i
            print(shoulderangle)
            if keyboard.is_pressed('w') == False:
                break
    while keyboard.is_pressed('s'):
        for i in range(shoulderangle, 0, -1):
            shoulderback(shoulderpin, i)
            shoulderangle = i
            print(shoulderangle)
            if keyboard.is_pressed('s') == False:
                break
    while keyboard.is_pressed('8'):
        for i in range(elbowangle, 180):
            elbowforward(elbowpin, i)
            elbowangle = i
            print(elbowangle)
            if keyboard.is_pressed('8') == False:
                break
    while keyboard.is_pressed('2'):
        for i in range(elbowangle, 0, -1):
            elbowback(elbowpin, i)
            elbowangle = i
            print(elbowangle)
            if keyboard.is_pressed('2') == False:
                break
    while keyboard.is_pressed('-'):
        for i in range(wristPangle, 0, -1):
            wristup(wristPpin, i)
            wristPangle = i
            print(wristPangle)
            if keyboard.is_pressed('-') == False:
                break
    while keyboard.is_pressed('+'):
        for i in range(wristPangle, 180):
            wristdown(wristPpin, i)
            wristPangle = i
            print(wristPangle)
            if keyboard.is_pressed('+') == False:
                break
    while keyboard.is_pressed('4'):
        for i in range(wristRangle, 180):
            wristleft(wristRpin, i)
            wristRangle = i
            print(wristRangle)
            if keyboard.is_pressed('4') == False:
                break
    while keyboard.is_pressed('6'):
        for i in range(wristRangle, 0, -1):
            wristright(wristRpin, i)
            wristRangle = i
            print(wristRangle)
            if keyboard.is_pressed('6') == False:
                break
