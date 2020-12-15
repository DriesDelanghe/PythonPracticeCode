class Product:
    def __init__(self, omschrijving, prijs):
        self.omschrijving = str(omschrijving)
        self.prijs = float(prijs)

    def toString(self):
        s = "Product {" + "omschrijving: " + str(self.omschrijving) + ", prijs: " + str(self.prijs) + "}"
        print(s)

    def increasePrice(self, AddToPrice):
        self.prijs += AddToPrice

    def increasePriceByOne(self):
        self.prijs += 1

    def doublePrice(self):
        self.prijs *= 2

    def halfPrice(self):
        self.prijs /= 2

    def increasePriceBy10Perc(self):
        self.prijs *= 1.1

    def decreasePriceBy20Perc(self):
        self.prijs *= 0.8

p1 = Product("banaan", 2)
p1.halfPrice()
p1.toString()

