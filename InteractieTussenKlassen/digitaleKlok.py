from src.InteractieTussenKlassen.Teller import Teller

class digitaleKlok:
    def __init__(self, uren, minuten, seconden):
        self.uren = uren
        self.minuten = minuten
        self.seconden = seconden

    def verhoogUren(self):
        if self.uren.getGetal() < 23:
            self.uren.verhoogGetal()
        else:
            self.uren.resetGetal()

    def verhoogMinuten(self):
        if self.minuten.getGetal() < 59:
            self.minuten.verhoogGetal()
        else:
            self.minuten.resetGetal()
            self.verhoogUren()

    def verhoogSeconden(self):
        if self.seconden.getGetal() < 59:
            self.seconden.verhoogGetal()
        else:
            self.seconden.resetGetal()
            self.verhoogMinuten()

    def __str__(self):
        return str(self.uren.getGetal()) +":"+ str(self.minuten.getGetal())+":"+ str(self.seconden.getGetal())