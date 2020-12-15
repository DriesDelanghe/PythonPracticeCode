class Product:

    def __init__(self, omschrijving, aantalInVoorraad, prijs):
        self.omschrijving = omschrijving
        self.aantalInVoorraad = aantalInVoorraad
        self.prijs = prijs

    def __str__(self):
        s=  "Product" + "\t" + "{" + "omschrijving:" + str(self.omschrijving) + "\t" + ", aantal in voorraad:" + str(self.aantalInVoorraad) + "\t" + ", prijs:" + str(self.prijs) + "}"
        return s


    def getOmschrijving(self):
        return self.omschrijving

    def getAantalInVoorraad(self):
        return self.aantalInVoorraad

    def getPrijs(self):
        return self.prijs

    def verhoogPrijsPerc(self, percentage):
        self.prijs = self.prijs*(1+(percentage/100))

