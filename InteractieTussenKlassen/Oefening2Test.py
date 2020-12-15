from src.InteractieTussenKlassen.Punt import Punt
from src.InteractieTussenKlassen.Lijnstuk import Lijnstuk

p1 = Punt(10,20)
p2 = Punt(20,50)

l1 = Lijnstuk(p1,p2)
print(l1.distance())
print(l1)
print(p1, p2)
