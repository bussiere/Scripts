fichier = open("hashcode.txt", "r")
toutesleslignes = fichier.readlines()

result = {}
i = 0
for ligne in toutesleslignes :
    i += 1
    try:
        test = float(ligne)
        test = True
    except ValueError:
        test = False
        print  ValueError
        print ligne
    if not test :
        temp = ligne
    else :
        
        try :
            if ligne not in  result[temp] :
                result[temp].append(ligne)
        except :
            result[temp] = []
            result[temp].append(ligne)

print result
        
    
