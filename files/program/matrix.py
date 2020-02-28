import random
import os
import sys
from time import sleep
try:
        sayi = int(sys.argv[1])
except:
        print "[*] Kodlari oku..."
        exit()


for i in range(sayi):
        os.system("xterm -e cmatrix &")
	sleep(0.6)
