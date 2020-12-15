class Teller:

    def __init__(self, getal, isUren): 
        self.getal = getal
        if(isUren):
            if getal > 0 or getal < 24:
                self.getal = getal
            else:
                self.getal = 0
        else:
            if getal > 0 or getal < 60:
                self.getal = getal
            else:
                self.getal = 0

    def verhoogGetal(self):
        self.getal += 1

    def resetGetal(self):
        self.getal = 0 

    def getGetal(self):
        return self.getal