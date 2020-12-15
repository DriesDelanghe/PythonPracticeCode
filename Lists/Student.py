class Student:
    def __init__(self, klas, naam):
        self.klas = klas
        self.naam = naam

    def getKlas(self):
        return self.klas

    def getNaam(self):
        return self.naam

    def __str__(self):
        return "Student{ klas:" + str(self.klas) + ", naam: " + str(self.naam)