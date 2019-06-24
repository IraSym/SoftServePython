class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side" + str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Quadrangle (Polygon):
    def __init__(self):
        print("Input sides of quadrangle")
        Polygon.__init__(self,4) 

    def findPerymetr(self):
        a, b, c, d = self.sides
        perymetr = (a + b + c + d) / (self.n)
        print('The perymetr of the quadrangle is %0.2f' %perymetr)

q=Quadrangle()
q.inputSides()
q.findPerymetr()
