import pyautogui
import keyboard
from time import sleep
import win32

def click(x,y):
    win32.win32api.SetCursorPos((x,y))
    win32.win32api.mouse_event(win32.win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.5)
    win32.win32api.mouse_event(win32.win32con.MOUSEEVENTF_LEFTUP, 0, 0)


pyautogui.click(1449,471) #to start the game
while keyboard.press('1') == False:  #if I press 1 the bot stops
    if pyautogui.pixelMatchesColor(1296,490,(0,0,0)):
        click(1296,490)
    if pyautogui.pixelMatchesColor(1396,488,(0,0,0)):
        click(1396,488)
    if pyautogui.pixelMatchesColor(1488,489,(0,0,0)):
        click(1488,489)
    if pyautogui.pixelMatchesColor(1580,486,(0,0,0)):
        click(1580,486)
    
