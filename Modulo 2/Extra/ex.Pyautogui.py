import pyautogui
import time
pyautogui.hotkey('win', 'r')
pyautogui.write('calc')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('8 + 2')
pyautogui.press('enter')