from random import randint

DICO = ["ENTRE", "OCTET", "FRUIT", "TAPIS", "PIECE", "PORTE", "VITRE", "NOTES", "BATON"]
Rang = randint(0, 8)
MOT = DICO[Rang]
ANS = False

i = 0

while i < 3 and ANS == False:
    REP = input("Un mot de 5 lettre:")

    if REP == MOT:
        ANS = True
    else:
        Compt = 0
        for j in range(0, 4):
            if MOT[j] == REP[j]:
                Compt = Compt+1
        print(Compt)

    i += 1

print(ANS, MOT)