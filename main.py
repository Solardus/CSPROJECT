from tkinter import *
import os as os
from msvcrt import *
import time
import math
import random

os.system("python get-pip.py")

x = 5
y = 5
lastPositionX = 0
lastPositionY = 0
coins = 0

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
def randGen(randXX,randYY):
    board[randYY][randXX] = '$'

def randomX():
    randx = random.randint(0,9)
    return randx

def randomY():
    randy = random.randint(0,9)
    return randy

randX = randomX()
randY = randomY()

randGen(int(randX),int(randY))

def printMap(lastX, lastY, y, x, coins):
    board[lastY][lastX] = '*'
    board[x][y] = '@'
    for row in board:
        for col in row:
            print(col, end=" ") # print each element separated by space
        if y == randX and x == randY:
            coins = coins + 1
            print("Coins: {}".format(coins))
            y = y - 1
            x = x - 1
            randX = randomX()
            randY = randomY()
            randGen(randX,randY)
        print() # Add newline

printMap(0,0,0,0,0)

while True:
    key = ord(getch())
    if key == 75:
        print("Left Arrow")
        lastPositionX = x
        lastPositionY = y
        x = x -1
        y = y
    if key == 77:
        print("Right Arrow")
        lastPositionX = x
        lastPositionY = y
        x = x +1
        y = y
    if key == 72:
        print("Up Arrow")
        lastPositionX = x
        lastPositionY = y
        x = x
        y = y -1
    if key == 80:
        print("Down Arrow")
        lastPositionX = x
        lastPositionY = y
        x = x
        y = y +1
    if key == 32:
        print("Space Key")
    if key == 13:
        print("Enter Key")
    if key == 105:
        print("i key")
    if key == 101:
        print("e key")
    if x == 10:
        x = 0
    if y == 10:
        y = 0
    printMap(lastPositionX, lastPositionY, x, y, coins)
    time.sleep(0.1)