import os
import pyautogui
import time
#os.system("chromium >> /dev/null")
#url adres cubuku konumu: 621, 74
pyautogui.click(x=621, y=74)
#link = "http://link.tl/1h7GN"
#iptal butonu konumu: 613, 480
#reklami gec konumu: 1273, 133
#sekme kapatma konumu: 383, 41
#yeni sekme acma konumu: 232, 42
def adresi_gir():
	pyautogui.typewrite("http://")
	pyautogui.typewrite("link.tl/")
	pyautogui.typewrite("1h7GN")
	pyautogui.press("enter")


def iptal():
	pyautogui.moveTo(613, 480, 3)
	pyautogui.click(x=613, y=480)


def reklami_gec():
	pyautogui.moveTo(1273, 133, 3)
	pyautogui.click(x=1273, y=133)

def sekmeyi_kapat():
	pyautogui.moveTo(383, 41, 4)
	pyautogui.click(x=383, y=41)


def sekme_ac():
	pyautogui.moveTo(232, 42, 4)
	pyautogui.click(x=232, y=42)



##ip adresi degistirme fonksiyonuda ekle sonra altdaki kodları while True ye al ve arkana yaslan
adresi_gir()
time.sleep(30)
iptal()
time.sleep(10)
reklami_gec()
time.sleep(30)
sekmeyi_kapat()
time.sleep(10)
sekme_ac()


s = raw_input("Emir bekliniyor...")
print pyautogui.position()
