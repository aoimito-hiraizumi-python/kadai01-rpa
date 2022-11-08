import pyautogui
import pyperclip
import time

pyautogui.keyDown("command")
pyautogui.press("space")
pyautogui.keyUp("command")

time.sleep(1)

pyautogui.write("google")

time.sleep(1)

pyautogui.press("enter")

time.sleep(1)

pyautogui.keyDown("command")
pyautogui.press("t")
pyautogui.keyUp("command")

time.sleep(1)

pyperclip.copy("平泉町 観光")
pyperclip.paste()

pyautogui.hotkey("command", "v")

time.sleep(1)

pyautogui.press("enter")

time.sleep(2)

pyautogui.hotkey("shift", "command", "3")
