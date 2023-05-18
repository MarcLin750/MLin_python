from random import randint

DICO = ["ENTRE", "OCTET", "FRUIT", "TAPIS", "PIECE", "PORTE", "VITRE", "NOTES", "BATON"]
Rang = randint(0, 8)
MOT = DICO[Rang]
longueur_mot = len(MOT)
ANS = False

print("La longueur du mot est:" , longueur_mot)

i = 0

while i < 3 and ANS == False:
    print("Saisir un mot de", longueur_mot ,"lettre:")
    REP = input()

    if REP == MOT:
        ANS = True
    else:
        Compt = 0
        for j in range(0, 4):
            if MOT[j] == REP[j]:
                Compt = Compt+1
        print(Compt)

    i += 1

print(MOT)

if REP == MOT:
    print("Bravo tu à trouver le bon mot !")

else:
    print("Le mot était: ", MOT)