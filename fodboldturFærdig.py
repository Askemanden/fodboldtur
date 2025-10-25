"""
    1.    Registrere modtagelse af betalinger
    2.    Udskrive liste over de indbetalte beløb samt angivelse af det beløb, som hvert medlem mangler at betale inden det fulde beløb er betalt, eller angivelse af, at det fulde beløb er betalt.
    3.    Gemme data.
    4.    Udskrive liste over de tre medlemmer, der mangler at betale mest.
"""
import pickle
from math import inf

filename = 'betalinger.pk'

TOTAL_BELØB = 4500

infile = open(filename,'rb')
fodboldtur : dict = pickle.load(infile)
infile.close()

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    BELØB_PR_PERSON = TOTAL_BELØB/len(fodboldtur)
    for navn, beløb in fodboldtur.items():
        print(navn)
        print(" indbetalt", beløb)
        if beløb >= BELØB_PR_PERSON:
            print(" mangler ingen inbetalinger")
        else:
            print(" mangler at indbetale", BELØB_PR_PERSON - beløb)
    
    

def indbetal():
    navn = input("Indtast navn af indbetalende person ")
    if (not navn in fodboldtur.keys()):
        print("Navn er ikke med\n")
        return
    betaling = input("Indtast beløb ")
    try:
        betaling = int(betaling)
    except Exception as e:
        print("Invalidt input ",e)
        return
    fodboldtur[navn] += betaling
    

def mindstBetalende():
    personer = {}
    for person, betalt in fodboldtur.items():
        if len(personer) < 3:
            personer[person] = betalt
            continue

        maxBeløb = ["", -float("inf")]
        for navn, beløb in personer.items():
            if beløb > maxBeløb[1]:
                maxBeløb = [navn, beløb]

        if betalt < maxBeløb[1]:
            personer.pop(maxBeløb[0])
            personer[person] = betalt

    print(personer)



def loop():
    running = True
    while running:
        print("MENU\n1: Print liste\n2: Indbetal\n3: Mindst betalende medlemmer\nE: End og gem")
        valg = input("Indtast dit valg: ")
        if (valg == '1'):
            printliste()
        elif (valg == "2"):
            indbetal()
        elif (valg == "3"):
            mindstBetalende()
        elif (valg == 'E'):
            afslut()
            running = False

if __name__ == "__main__":
    loop()