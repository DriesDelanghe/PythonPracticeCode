class OpleidingsOnderdeel:
    def __init__(self, punten, naam):
        self.punten = punten
        self.naam = naam

    def getNaam(self):
        return self.naam

    def getPunten(self):
        return self.punten

    def __str__(self):
        return "Opleidingsonderdeel { naam:" + str(self.naam) + ", score:" + str(self.punten) + "}"

