import socket
import sys
import time


try:
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = sys.argv[1]
        port = int(sys.argv[2])
        socket.bind((host, port))
        print "basladi"
        socket.listen(5)
        misafir, kim = socket.accept()
        print "baglandi:", kim
        try:
                print "deniyor..."
                misafir.send("selam")
                data = misafir.recv(1024)
                print data
        except:
                print "olmadi"
                socket.close()
                exit()
        b = "\n" + "-" * 20 + "\n"

        while True:
                cod = raw_input("message ::>")
                if cod == "Q":
                        misafir.send("Q")
                        misafir.close()
                        break
                else:
                        misafir.send(cod)
                        print "okunuyor...."
                        try:
                                ret = misafir.recv(1024)
                                if not ret:
                                        pass
                                else:
                                        print b + ret
                        except:
                                print "bostu galiba..."
except:
        print "cikildi..."
        socket.close()
