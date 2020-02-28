import pyautogui
import time
konum = pyautogui.position()
print konum
print "cikmak icin Control-c yapiniz..."


try:
	while True:
		time.sleep(0.001)
		if konum != pyautogui.position():
			pyautogui.moveTo(konum)
except:
	print "cikildi..."
