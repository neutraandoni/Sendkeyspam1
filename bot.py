import pyautogui
import time

print("Type 'c' to start")
Y = input()
if(Y == "c"):
    print("3 second delay...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    f = open("txt", 'r')
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        print("Injected", word)
    print("Done!")
else:
    print("k")










