from src.Lists.Magazijn import Magazijn
from src.Lists.Product import Product

m1 = Magazijn("2800")

p1 = Product("peren", 3, float(5))
p2 = Product("appelen", 17, float(3))
p3 = Product("bananen", 17, float(2))

m1.addProduct(p1)
m1.addProduct(p2)
m1.addProduct(p3)

print(m1)
m1.IncreasePrice(50)
print(m1)
m1.showListToStock()
