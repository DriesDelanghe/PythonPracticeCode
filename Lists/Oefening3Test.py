from src.Lists.Student import Student
from src.Lists.Rapport import Rapport
from src.Lists.OpleidingsOnderdeel import OpleidingsOnderdeel

o1 = OpleidingsOnderdeel(10,"Frans");
o2 = OpleidingsOnderdeel(11,"Java");
o3 = OpleidingsOnderdeel(10,"Databanken");
studJan = Student("1IMSA","Jan");
rapJan = Rapport(studJan);
rapJan.voegToe(o1);
rapJan.voegToe(o2);
rapJan.voegToe(o3);
print(rapJan);
