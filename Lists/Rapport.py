class Rapport:
    def __init__(self, student):
        self.student = student
        self.vakList = list()

    def voegToe(self, vak):
        self.vakList.append(vak)

    def __str__(self):
        s = "Rapport " + str(self.student) +"\n" + "vakken: \n"

        for vak in self.vakList:
            s+= "\t" + str(vak) +"\n"

        return s