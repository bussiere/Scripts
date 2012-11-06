f = open("arduino_jumper_cable_1_600.png", "rb")
data = f.read()
base = data.encode("base64")
print base
f = open('resultbase64.txt', 'w')
f.write(base)
f.close()