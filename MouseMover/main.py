import pyautogui
import time

pyautogui.FAILSAFE = False

end_time = int(input("Enter minutes value (it will run for that many minutes!) : "))
max_value = 60*end_time

while end_time > 0:
    time.sleep(300)
    for i in range(0, 50):
        pyautogui.moveTo(0, i*5)
    for key in range(0, 1):
        pyautogui.press('shift')
    end_time -= 1

print("Execution is finished!!")
