from src.InteractieTussenKlassen.Afdeling import Afdeling
from src.InteractieTussenKlassen.Bediende import Bediende

a1 = Afdeling("Boekhouden", "Brussel")
a2 = Afdeling("Verkoop", "Antwerpen")

b1 = Bediende("Mieke", 3300)
b2 = Bediende("Marina", 2500)

b1.setAfdeling(a2)
b2.setAfdeling(a1)

b1.verhoogSalaris(2000)
b2.verhoogSalaris(100)

print(b1)
print(b2)