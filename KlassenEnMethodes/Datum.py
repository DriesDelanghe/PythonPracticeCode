class Datum:

    def __init__(self, dag, maand, jaar):
        self.dag = dag
        self.maand = maand
        self.jaar = maand

    def printDate(self):
        s=str(self.dag) +  "/" + str(self.maand) + "/" + str(self.jaar)
        print(s)


d1 = Datum(20, 10, 1998)
d2 = Datum(9, 12, 2020)
d1.printDate()
d2.printDate()

