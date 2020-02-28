g = ""
while True:
	mesaj = raw_input("| ")
	if mesaj != "q":
		g += mesaj + "\n"
	else:
		break

print g
