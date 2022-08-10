
import pyautogui, time

message = input("message: ")
duration = input("duration: ")
repeats = input("repeats: ")

time.sleep(5)

for i in range(int(repeats)):
    pyautogui.write(message)
    pyautogui.press('enter')
    time.sleep(int(duration))