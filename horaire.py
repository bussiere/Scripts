

def additionheure(heuredebut,heurefin):
	tabdebut = heuredebut.split(":")
	tabfin = heurefin.split(":")
	ajout = 0
	minute = int(tabdebut[1])+int(tabfin[1])
	if minute >= 60 :
		ajout += 1
		minute =  minute - 60
	if minute < 10 :
		minute = "0%d"%minute
	heure = int(tabdebut[0])+int(tabfin[0]) + ajout
	minute = str(minute)
	heure = str(heure)
	return "%s:%s"%(heure,minute)

def soustractionheure(heurefin,heuredebut):
	tabdebut = heuredebut.split(":")
	tabfin = heurefin.split(":")
	ajout = 0
	minute = int(tabfin[1])-int(tabdebut[1])
	if minute < 00 :

		ajout -= 1
		minute =  minute + 60
	if minute < 10 :
		minute = "0%d"%minute
	heure = int(tabfin[0]) - int(tabdebut[0]) + ajout
	minute = str(minute)
	heure = str(heure)
	return "%s:%s"%(heure,minute)


def horaire(debut,pausemidi="1:00",total="7:45"):
	plusmidi = additionheure(debut,pausemidi)
	return additionheure(plusmidi,total)

def entrop(fin,debut,pausemidi="0:45",total="7:45"):
	plusmidi = additionheure(debut,pausemidi)
	return soustractionheure(fin,plusmidi)

def maxheure(debut,pausemidi="0:45",total="10:00"):
	return horaire(debut,pausemidi,total)



	
print horaire("9:00")
print entrop("19:00","09:00")


# print additionheure("10:50","8:15")
# print maxheure("7:30")




