class Afdeling:

    def __init__(self, naam, locatie):
        self.naam = str(naam)
        self.locatie = str(locatie)

    def getNaam(self):
        return self.naam

    def getLocatie(self):
        return self.locatie

    def setLocatie(self, locatie):
        self.locatie = locatie

    def setNaam(self, naam):
        self.naam = naam

