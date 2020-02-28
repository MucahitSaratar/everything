import subprocess



def run(command):
	kod = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
	return kod.stdout.read() #.replace("\n", "")



dizin = run("pwd")
username = run("whoami")

satir = username + "@trregen:" + dizin + "$ "

while True:
	komut = raw_input(satir.replace("\n", ""))
	if komut == "exit":
		run("exit")
	calistir = run(komut)
	print calistir
