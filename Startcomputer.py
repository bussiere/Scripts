import os
import os
import datetime
import random
message = "start a : "
now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M"))
os.chdir("C:\\AtelierSODA\\workspaceSODA\\madrhas")
os.system("echo heure de start %s >> C:\\AtelierSODA\\workspaceSODA\\madrhas\\startcxomputer.txt"%(now))
os.system("git add . >> C:\\AtelierSODA\\logadd.txt")
os.system("git commit -m '%s %s' >> C:\\AtelierSODA\\logcommit.txt"%(now,message))
os.system("C:\\AtelierSODA\\IDE\\eclipse\\eclipse.exe")
os.system("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
os.system("exit")