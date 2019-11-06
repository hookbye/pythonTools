#-*- coding:UTF-8-*-
import win32api
import win32con
import time
import sys
import msvcrt
import pyHook
import pythoncom
import threading

lukyDrawPos = [-1920+850,750]
vipPos = [[-1920+1033,641],[-1920+850,606]]

TO_EXIT = False
def LeftClick(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
def KeyInput(keyCode):
    pass
def KeyDown(event):
    TO_EXIT = True
    print("any key down..",event)
    return True
    
if __name__ == "__main__":
    # hookManager = pyHook.HookManager()
    # hookManager.KeyDown = KeyDown
    # hookManager.HookKeyboard()
    # thread1 = threading.Thread(target=pythoncom.PumpMessages, args=("thread 1",))
    # thread1.start()
    for i in range(1,20):
        LeftClick(-1920+745,830)
        time.sleep(1)
        # LeftClick(-1920+850,606)
        # time.sleep(0.1)
        print("click ....",i)
        
        if TO_EXIT:
            break
    # pythoncom.PumpMessages()
    input()
    pass
    