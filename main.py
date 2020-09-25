import pyautogui
import time

pyautogui.FAILSAFE = False

# this loop will run for 3 times.
# for i in range(0, 1):
time.sleep(4)
pyautogui.press('q')
time.sleep(5)
pyautogui.typewrite('Arafat Hossain')
time.sleep(5)
pyautogui.press('down')
time.sleep(4)
pyautogui.press('enter')
time.sleep(5)
pyautogui.typewrite('Hi Arafat')
time.sleep(2)
pyautogui.press('enter')
time.sleep(3)
pyautogui.typewrite('This is a Test Message.')
time.sleep(3)
pyautogui.press('enter')