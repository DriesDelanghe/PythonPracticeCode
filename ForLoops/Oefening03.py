beginGetal = int(input("Geef begin getal: "))
eindGetal = int(input("Geef eind getal:"))

rangeNr = eindGetal - beginGetal

for i in range(rangeNr + 1):
    if((beginGetal + i)%2 == 0):
        s = "het kwadraat van " + str(beginGetal + i) + " is " + str((beginGetal + i)**2) + "\n"
        print(s)
