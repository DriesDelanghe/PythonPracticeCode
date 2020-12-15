import math
from src.InteractieTussenKlassen.Punt import Punt 

class Lijnstuk:

    def __init__(self, beginPunt, eindPunt):
        self.beginPunt = beginPunt
        self.eindPunt = eindPunt

    def getBeginPunt(self):
        return self.beginPunt

    def getEindPunt(self):
        return self.eindPunt

    def setBeginPunt(self, punt):
        self.beginPunt = punt

    def setEindPunt(self, punt):
        self.eindPunt = punt

    def __str__(self):
        return "(" + str(self.beginPunt.x) + "," + str(self.beginPunt.y) + ") - (" + str(self.eindPunt.x) + "," +str(self.eindPunt.y) + ")"

    def distance(self):
        afstand = math.sqrt((self.eindPunt.x - self.beginPunt.x)**2 + (self.eindPunt.y - self.beginPunt.y)**2)

        return afstand