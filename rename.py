import os
liste = []
import sys

for root, dirs, files in os.walk(sys.argv[1]):
	for fil in files :
		liste.append(root+"/"+fil)

print liste

if len(sys.argv) == 4 :
	replace = sys.argv[3]
else :
	replace = ""
for fil in liste :
	os.rename(fil, fil.replace(sys.argv[2],replace))