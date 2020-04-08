from tkinter import *
import pyautogui
#---------------------------------------------------------------------
root = Tk()
root.title("PCAwaker")
root.geometry("300x250")
#---------------------------------------------------------------------
#"""FAILSAFE is set to false inorder to avoid (1,1) location error """
pyautogui.FAILSAFE = False
varStatus = StringVar()
varStatus.set("Status: Running....")
running = True  # Global running flag
varClose = True # Global closing flag
idx = 0  # loop index
#---------------------------------------------------------------------
def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True
    varStatus.set("Status: Running....")
def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
    varStatus.set("Status: Stopped!")
def close():
    global varClose
    root.quit()
    varClose = False
#---------------------------------------------------------------------
Button(root, text="Start", command=start).grid(row=0, column=1, padx=120, pady=10)
Button(root, text="Stop", command=stop).grid(row=4, column=1, padx=120, pady=10)
Button(root, text="Close", command=close).grid(row=6, column=1, padx=120, pady=10)
Label(root, textvariable=varStatus).grid(row=7, column=1)
#---------------------------------------------------------------------
while varClose:
    if idx % 10 == 0:
		#Update the UI once in a while
        root.update()
    if running:
        idx += 1
        if idx == 2:
            print("Mouse Movement")
            for i in range(0,10):
                pyautogui.moveTo(0,i*10)
                print(str(i)+" And "+ str(idx))
            pyautogui.moveTo(1,1)
            for i in range(0,3):
                pyautogui.press("shift")

    if idx == 50000000:
        idx = 0
#---------------------------------------------------------------------
