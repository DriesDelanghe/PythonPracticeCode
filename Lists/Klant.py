class Klant:
    def __init__(self, naam, postcode):
        self.naam = naam
        self.postcode = postcode
        self.artikelList = list()

    def koop(self, artikel):
        self.artikelList.append(artikel)

    def maakKassaticket(self):
        s = "naam:" + str(self.naam) + "\t" + "postcode:" + str(self.postcode) + "\n" + "\t" + "Artikels: \n"

        for artikel in self.artikelList:
            s += "\t\t" + str(artikel) + "\n"

        return s

    def __str__(self):
        return self.maakKassaticket()

    def bepaalGoedkoopste(self):
        
        laagstePrijs = self.artikelList[0].getPrijsInclusiefBTW()
        goedkoopsteArtikel = self.artikelList[0]
        for artikel in self.artikelList:
            if(artikel.getPrijsInclusiefBTW() < laagsteprijs):
                goedkoopsteArtikel = artikel

        return goedkoopsteArtikel

    
    def bepaalDuurste(self):
        hoogstePrijs = self.artikelList[0].getPrijsInclusiefBTW
        duursteArtikels = list()
        
        for artikel in self.artikelList:
            if(artikel.getPrijsInclusiefBTW() > hoogstePrijs):
                hoogstePrijs = artikel.getPrijsInclusiefBTW()

        for artikel in self.artikelList:
            if(artikel.getPrijsInclusiefBTW() == hoogstePrijs):
                duursteArtikels.append(artikel)
        
        return duursteArtikels
