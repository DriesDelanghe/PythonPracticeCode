from src.InteractieTussenKlassen.Teller import Teller
from src.InteractieTussenKlassen.digitaleKlok import digitaleKlok

t1 = Teller(23, True)
t2 = Teller(59, False)
t3 = Teller(59, False)


d = digitaleKlok(t1,t2,t3)

d.verhoogSeconden()
d.verhoogMinuten()
d.verhoogUren()
print(d)


