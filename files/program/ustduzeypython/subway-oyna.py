import pyautogui
pyautogui.moveTo(610, 403)
import pyxhook
import time


def W():
        pyautogui.mouseDown(button='left')
	pyautogui.moveRel(None, -1 * 40)
	pyautogui.mouseUp(button='left',)
        pyautogui.moveTo(610, 403)

def A():
        pyautogui.mouseDown(button='left')
        pyautogui.moveRel(-1 * 40, None)
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(610, 403)


def S():
        pyautogui.mouseDown(button='left')
        pyautogui.moveRel(None, 40)
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(610, 403)


def D():
        pyautogui.mouseDown(button='left')
        pyautogui.moveRel(40, None)
        pyautogui.mouseUp(button='left')
        pyautogui.moveTo(610, 403)


def kbevent(event):
    global running
    if event.Ascii == 113:
        running = False
    elif event.Ascii == 119:
	W()
    elif event.Ascii == 97:
	A()
    elif event.Ascii == 115:
	S()
    elif event.Ascii == 100:
	D()



hookman = pyxhook.HookManager()

hookman.KeyDown = kbevent

hookman.HookKeyboard()

hookman.start()


running = True
while running:
    time.sleep(0.1)


hookman.cancel()
