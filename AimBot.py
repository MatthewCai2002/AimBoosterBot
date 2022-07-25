from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    img = pyautogui.screenshot(region=(495,314,905, 635))
    width, height = img.size
    # rgb = 255, 219, 195
    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r,g,b = img.getpixel((x,y))
            if r== 255 and b == 195 and g == 219:
                click(x + 495, y + 314)
                
                break
