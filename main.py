from tkinter import *
import os as os
from msvcrt import *
import time

os.system("python get-pip.py")

x = 0
y = 0
lastPosition = 0

board = [['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*']]
#10x10

for row in board:
    for col in row:
        print(col, end=" ") # print each element separated by space
    print() # Add newline

#while True:
    #if getk
while True:
    key = ord(getch())
    if key == 75:
        print("Left Arrow")
    if key == 77:
        print("Right Arrow")
    if key == 72:
        print("Up Arrow")
    if key == 80:
        print("Down Arrow")
    if key == 32:
        print("Space Key")
    if key == 13:
        print("Enter Key")
    if key == 105:
        print("i key")
    if key == 101:
        print("e key")
    time.sleep(0.1)