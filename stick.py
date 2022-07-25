import pyautogui
import time

time.sleep(2)
img = pyautogui.screenshot(region=(495,314,905, 635))
img.save(r"C:\Users\David\Desktop\Coding\scripts\AimBot\savedImage.png")
