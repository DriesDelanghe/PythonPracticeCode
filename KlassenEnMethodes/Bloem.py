class Bloem:

    def __init__(self, naam, kleur, stukprijs):
        self.naam = naam
        self.kleur = kleur
        self.stukPrijs = stukprijs


    def drukAf(self):
        s = self.naam + " heeft als kleur " + self.kleur + " en kost " + str(self.stukPrijs)
        print(s)

    def changeColour(self, kleur):
        self.kleur = kleur


b1 = Bloem("tulp", "rood", 2)
b2 = Bloem("roos", "geel", 3)
b1.drukAf()
b2.drukAf()

b1.changeColour("geel")
b1.drukAf()
