import os
import datetime
import random
character = ["Yuki", "Haruhi", "Mikuru"]
now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M"))
os.chdir("C:\\AtelierSODA\\workspaceSODA\\madrhas")
os.system("git add .")
os.system("git commit -m '%s %s'"%(now,character[random.randint(0,  len(character)-1)]))


