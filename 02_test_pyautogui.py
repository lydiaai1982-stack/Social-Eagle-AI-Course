import pyautogui
import time

#give yourself a few seconds to hover over the target

time.sleep (5)

x,y = pyautogui.position()

print (f"mouse is at ({x}, {y})")

