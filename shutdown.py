import os
import os
import datetime
import random
message = "Shutdown a : "
now = datetime.datetime.now()
now = str(now.strftime("%Y-%m-%d %H:%M"))
os.chdir("C:\\AtelierSODA\\workspaceSODA\\madrhas")
os.system("echo heure de shtudown %s >> C:\\AtelierSODA\\workspaceSODA\\madrhas\\shutdown.txt"%(now))
os.system("git add . >> C:\\AtelierSODA\\logadd.txt")
os.system("git commit -m '%s %s' >> C:\\AtelierSODA\\logcommit.txt"%(now,message))
os.system("shutdown -s -t 00")
