from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('stickman.png', confidence=0.8, region=(840,375,250,330), grayscale=True) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I can't see it")
        time.sleep(0.5)
