import os
import sys

uid = sys.argv[1]
at = sys.argv[2]
url = "https://api.instagram.com/v1/users/" + uid + "/followed-by/?" + at
kod = "curl " + url
os.system(kod)
