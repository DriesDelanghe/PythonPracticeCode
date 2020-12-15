from src.InteractieTussenKlassen.Afdeling import Afdeling

class Bediende:
    def __init__(self, naam, salaris):
        self.naam = naam
        self.salaris = salaris

    def getNaam(self):
        return self.naam

    def getSalaris(self):
        return self.naam

    def getAfdeling(self):
        return self.afdeling

    def setNaam(self, naam):
        self.naam = naam

    def setSalaris(self, salaris):
        self.salaris = salaris

    def setAfdeling(self, afdeling):
        self.afdeling = afdeling

    def verhoogSalaris(self, verhoging):
        if verhoging > self.salaris*0.1 :
            self.salaris += self.salaris*0.1
            print("salaris kan niet met meer dan 10% verhoogt worden")
        else:
            self.salaris += verhoging

    def __str__(self):
        return str(self.naam) + " verdient " + str(self.salaris) + " en is werkzaam in " + self.afdeling.naam + " op de locatie " + self.afdeling.locatie