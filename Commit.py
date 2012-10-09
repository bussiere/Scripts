import os
import datetime
import random
character = ["Yuki", "Haruhi", "Mikuru"]
now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M"))
os.chdir("C:\\AtelierSODA\\workspaceSODA\\madrhas")
os.system("git add . >> C:\\AtelierSODA\\logadd.txt")
os.system("git commit -m '%s %s' >> C:\\AtelierSODA\\logcommit.txt"%(now,character[random.randint(0,  len(character)-1)]))


