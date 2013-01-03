fichier = open("is.txt", "r")
toutesleslignes = fichier.readlines()
fichier2 = open("boolean.txt", "r")
toutesleslignes2 = fichier2.readlines()

result = []
i = 0
for ligne in toutesleslignes :
    ligne = ligne.replace("\r","")
    ligne = ligne.replace("\n","")
    #print toutesleslignes2[i]
    if 'true' in toutesleslignes2[i] :
        t = "assertTrue(applicationWeb2.%s);\n"%(ligne)
    else :
        t = "assertFalse(applicationWeb2.%s);\n"%(ligne)
    result.append(t)
    print t
    i += 1
   
print result

fichier.close()
fichier2.close()
