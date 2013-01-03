fichier = open("is.txt", "r")
toutesleslignes = fichier.readlines()

result = []
for ligne in toutesleslignes :
    ligne = ligne.replace("\r","")
    ligne = ligne.replace("\n","")
    t = "System.out.println(applicationWeb2.%s);\n"%(ligne)
    result.append(t)
    print t
   
print result
        
    
