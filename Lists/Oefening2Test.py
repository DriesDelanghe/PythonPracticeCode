from src.Lists.Klant import Klant
from src.Lists.Artikel import Artikel

a1 = Artikel("nutella 500g", 3, 21)
a2 = Artikel("papier voor printer 500 vellen", 10, 21)
a3 = Artikel("paprika mixed", 4, 6)

k = Klant("Van Den Bosch", "2820")

k.koop(a1)
k.koop(a2)
k.koop(a3)

print(a1)

print("\nkassaticket aan het maken")

(k.maakKassaticket())

print("\nkassaticket tonen")

print(k)