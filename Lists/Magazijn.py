from src.Lists.Product import Product

class Magazijn:

    products = list()

    def __init__(self, postcode):
        self.postcode = postcode

    def addProduct(self, product):
        self.products.append(product)

    
    def __str__(self):   
        s = "Magazijn at " + str(self.postcode) + " \n" + "\t" + "{" +"\n" +"\t"

        for product in self.products:
            s += "\t" + str(product)
            s += "\n" + "\t"

        s+= "}"

        return s

    def IncreasePrice(self, increasePercentage):

        for product in self.products:
            product.verhoogPrijsPerc(increasePercentage)

    def showListToStock(self):
        for product in self.products:
            if(product.getAantalInVoorraad() < 5):
                print(str(product.getOmschrijving()), str(product.getAantalInVoorraad()))