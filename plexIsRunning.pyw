from requests import get
import win32gui
import win32api
import win32con
from random import randint
from datetime import datetime
from config import PLEX_TOKEN


def checkIfRunning():
    try:
        r = get(
            f"http://localhost:32400/status/sessions?X-Plex-Token={PLEX_TOKEN}")
        if ('<MediaContainer size="0">' in r.text):
            return False
        return True
    except:
        return False


def moveCursor():
    flags, hcursor, (x, y) = win32gui.GetCursorInfo()
    newY = y+randint(-100, 100)
    newX = x+randint(-100, 100)
    win32api.SetCursorPos((newX, newY))


def pressKey():
    win32api.keybd_event(0x0D, 0, 0, 0)
    win32api.keybd_event(0x0D, 0, win32con.KEYEVENTF_KEYUP, 0)


if(checkIfRunning()):
    pressKey()
    moveCursor()
    moveCursor()
    pressKey()

