class Artikel:
    def __init__(self, omschrijving, nettoprijs, btwPercentage):
        self.omschrijving = omschrijving
        self. nettoprijs = nettoprijs
        self.btwPercentage = btwPercentage



    def getOmschrijving(self):
        return self.omschrijving

    def getNettoPrijs(self):
        return self.nettoprijs

    def getBTWPercentage(self):
        return self.btwPercentage

    def getPrijsInclusiefBTW(self):
        prijsBTW = self.nettoprijs * (1 + (self.btwPercentage/100))
        return prijsBTW

    def __str__(self):
        s= "artikel {" + "omschrijving:" + str(self.omschrijving) + ",\t" + "netto prijs:" + str(self.nettoprijs)+ ",\t" + "prijs met btw:" + str(self.getPrijsInclusiefBTW()) + "}"
        return s

