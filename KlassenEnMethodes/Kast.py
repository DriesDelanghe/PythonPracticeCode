class Kast:
    def __init__(self, hoogte, breedte, diepte):
        self.hoogte = int(hoogte)
        self.breedte = int(breedte)
        self.diepte = int(diepte)

    def printKast(self):
        s = "De kast is: \n \n" +  str(self.hoogte) + " hoog \n" +  str(self.breedte) + " breed \n" +  str(self.diepte) + " diep \n"
        print(s)

    def berekendVooraanzicht(self):
        Opp = self.breedte * self.hoogte
        s = "De oppervlakte van het vooraanzicht is: " + str(Opp)
        print(s)

    def GetHoogte(self):
        return self.hoogte

    def GetBreedte(self):
        return self.breedte

    def GetDiepte(self):
        return self.diepte

    def setHoogte(self, hoogte):
        self.hoogte = hoogte

    def setBreedte(self, breedte):
        self.breedte = breedte

    def setDiepte(self, diepte):
        self.diepte = diepte
        
    

k1 = Kast(117, 69, 43)
k2 = Kast(177,32,29)
k3 = Kast(187,69,30)

k1.printKast()
k2.printKast()
k3.printKast()

print(str(k1.GetBreedte()))

k3.setBreedte(5)
k3.printKast()

k2.berekendVooraanzicht()


