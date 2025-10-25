"""
    1.    Registrere modtagelse af betalinger
    2.    Udskrive liste over de indbetalte beløb samt angivelse af det beløb, som hvert medlem mangler at betale inden det fulde beløb er betalt, eller angivelse af, at det fulde beløb er betalt.
    3.    Gemme data.
    4.    Udskrive liste over de tre medlemmer, der mangler at betale mest.
"""
import pickle

filename = 'betalinger.pk'

fodboldtur ={}

def afslut():
    outfile = open(filename, 'wb')
    pickle.dump(fodboldtur, outfile)
    outfile.close()
    print("Programmet er afsluttet!")

def printliste():
    for item in fodboldtur.items():
        print(item[0])
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Afslut program")
    valg = input("Indtast dit valg:")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        afslut()

infile = open(filename,'rb')
fodboldtur = pickle.load(infile)
infile.close()
menu()

