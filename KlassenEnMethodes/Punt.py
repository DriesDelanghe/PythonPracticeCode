class Point:
    
    def __init__ (self, x, y):
        self.x = float(x)
        self.y = float(y)

    def printPoint(self):
        s = "(" + str(self.x) +", " + str(self.y) +")"
        print(s)

p1 = Point(2,5.5)
p2 = Point(3.5, 3.78)

p1.printPoint()
p2.printPoint()
